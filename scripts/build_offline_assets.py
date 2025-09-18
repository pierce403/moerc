#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Iterable, List

ROOT = Path(__file__).resolve().parent.parent
MANUAL_MD = ROOT / "MOERC-Build-Manual-v0.1.md"
ATTACHMENTS_DIR = ROOT / "modules/ROOT/assets/attachments"
STATIC_DOWNLOADS_DIR = ROOT / "supplemental-ui/static/downloads"
PDF_PATH = ATTACHMENTS_DIR / "moerc-build-guide-v0.1.pdf"
BOM_CSV = ATTACHMENTS_DIR / "moerc-bom-v0.1.csv"

PAGE_WIDTH = 612  # 8.5in at 72 dpi
PAGE_HEIGHT = 792  # 11in at 72 dpi
MARGIN_X = 54
MARGIN_Y = 54
LINE_HEIGHT = 14
CHARS_PER_LINE = 90


def ensure_output_dir() -> None:
    ATTACHMENTS_DIR.mkdir(parents=True, exist_ok=True)
    STATIC_DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)


def strip_markdown(markdown_text: str) -> str:
    text = markdown_text.replace("\r\n", "\n")
    # Remove code fences
    text = re.sub(r"```.*?```", lambda m: m.group(0).replace("`", ""), text, flags=re.S)
    # Drop heading and blockquote markers
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
    # Strip list markers
    text = re.sub(r"^\s{0,3}[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s{0,3}\d+\.\s+", "", text, flags=re.MULTILINE)
    # Convert links and images
    text = re.sub(r"!\[(.*?)\]\((.*?)\)", r"\1", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", text)
    # Strip emphasis markers
    text = re.sub(r"[*_`]", "", text)
    # Collapse multiple spaces
    text = re.sub(r"[ \t]+", " ", text)
    return text


def convert_markdown_to_lines(markdown_path: Path) -> List[str]:
    raw = markdown_path.read_text(encoding="utf-8")
    stripped = strip_markdown(raw)
    lines: List[str] = []
    for line in stripped.splitlines():
        line = line.rstrip()
        if not line:
            lines.append("")
            continue
        wrapped = wrap_text(line, CHARS_PER_LINE)
        lines.extend(wrapped)
    if not lines:
        lines.append("")
    return lines


def wrap_text(text: str, width: int) -> List[str]:
    words = text.split(" ")
    wrapped: List[str] = []
    current: List[str] = []
    current_length = 0
    for word in words:
        if not current:
            current = [word]
            current_length = len(word)
            continue
        if current_length + 1 + len(word) <= width:
            current.append(word)
            current_length += 1 + len(word)
        else:
            wrapped.append(" ".join(current))
            current = [word]
            current_length = len(word)
    if current:
        wrapped.append(" ".join(current))
    return wrapped


def chunk_lines(lines: Iterable[str], per_page: int) -> List[List[str]]:
    pages: List[List[str]] = []
    current: List[str] = []
    for line in lines:
        current.append(line)
        if len(current) >= per_page:
            pages.append(current)
            current = []
    if current:
        pages.append(current)
    return pages or [[""]]


def escape_pdf_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build_content_stream(page_lines: List[str]) -> bytes:
    start_y = PAGE_HEIGHT - MARGIN_Y
    lines = ["BT", "/F1 12 Tf", f"{LINE_HEIGHT} TL", f"1 0 0 1 {MARGIN_X} {start_y} Tm"]
    for line in page_lines:
        if line:
            lines.append(f"({escape_pdf_text(line)}) Tj")
        lines.append("T*")
    lines.append("ET")
    payload = "\n".join(lines).encode("utf-8")
    return f"<< /Length {len(payload)} >>\nstream\n".encode("utf-8") + payload + b"\nendstream"


def write_pdf(lines: List[str], pdf_path: Path) -> None:
    lines_per_page = max(1, int((PAGE_HEIGHT - 2 * MARGIN_Y) / LINE_HEIGHT))
    pages = chunk_lines(lines, lines_per_page)

    objects: List[bytes | None] = [None]

    def new_object(data: bytes | None = None) -> int:
        objects.append(data)
        return len(objects) - 1

    def set_object(index: int, data: bytes) -> None:
        objects[index] = data

    catalog_obj = new_object()
    pages_obj = new_object()
    font_obj = new_object(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    page_entries: List[tuple[int, int]] = []
    for page in pages:
        content_obj = new_object(build_content_stream(page))
        page_obj = new_object()
        page_entries.append((page_obj, content_obj))

    kids = " ".join(f"{page_obj} 0 R" for page_obj, _ in page_entries) or ""
    set_object(pages_obj, f"<< /Type /Pages /Kids [{kids}] /Count {len(page_entries)} >>".encode("utf-8"))

    for page_obj, content_obj in page_entries:
        set_object(
            page_obj,
            f"<< /Type /Page /Parent {pages_obj} 0 R /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] /Resources << /Font << /F1 {font_obj} 0 R >> >> /Contents {content_obj} 0 R >>".encode(
                "utf-8"
            ),
        )

    set_object(catalog_obj, f"<< /Type /Catalog /Pages {pages_obj} 0 R >>".encode("utf-8"))

    with pdf_path.open("wb") as fh:
        fh.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets: List[int] = []
        for index in range(1, len(objects)):
            obj_data = objects[index]
            if obj_data is None:
                obj_data = b"<<>>"
            offsets.append(fh.tell())
            fh.write(f"{index} 0 obj\n".encode("utf-8"))
            fh.write(obj_data)
            fh.write(b"\nendobj\n")
        xref_pos = fh.tell()
        fh.write(f"xref\n0 {len(objects)}\n".encode("utf-8"))
        fh.write(b"0000000000 65535 f \n")
        for offset in offsets:
            fh.write(f"{offset:010d} 00000 n \n".encode("utf-8"))
        fh.write(b"trailer\n")
        fh.write(f"<< /Size {len(objects)} /Root {catalog_obj} 0 R >>\n".encode("utf-8"))
        fh.write(f"startxref\n{xref_pos}\n%%EOF".encode("utf-8"))


def sync_static_downloads(files: Iterable[Path]) -> None:
    for source in files:
        if not source.exists():
            raise FileNotFoundError(f"Missing offline asset: {source}")
        destination = STATIC_DOWNLOADS_DIR / source.name
        shutil.copy2(source, destination)


def main() -> None:
    ensure_output_dir()
    lines = convert_markdown_to_lines(MANUAL_MD)
    write_pdf(lines, PDF_PATH)
    sync_static_downloads([PDF_PATH, BOM_CSV])


if __name__ == "__main__":
    main()
