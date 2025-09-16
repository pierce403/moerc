SHELL := /usr/bin/bash

.PHONY: all clean install site preview

NODE_BIN := ./node_modules/.bin
BUILD_DIR := build
SITE_DIR := $(BUILD_DIR)/site

all: site

install:
	npm ci || npm install

site:
	$(NODE_BIN)/antora antora-playbook.yml || npx antora antora-playbook.yml

preview: site
	npx http-server $(SITE_DIR) -p 8080 -c-1

clean:
	rm -rf $(BUILD_DIR)