# MOERC Build Guide

Metal-Oxide Electrolysis Refinement Chamber - Step-by-Step Build Guide

## Overview

This repository contains a comprehensive build guide for constructing a Metal-Oxide Electrolysis Refinement Chamber (MOERC). The guide is organized as a step-by-step manual using the Antora documentation platform.

## Building the Documentation

### Prerequisites

- Node.js (version 16 or higher)
- npm (Node Package Manager)

### Quick Start

1. Install dependencies:
   ```bash
   npm install
   ```

2. Build the documentation site:
   ```bash
   npm run build:site
   ```

3. Preview the site locally:
   ```bash
   npm run preview
   ```

   The site will be available at http://localhost:8080

### Make Commands

Alternatively, you can use the provided Makefile:

```bash
# Install dependencies
make install

# Build the site
make site

# Preview locally
make preview

# Clean build artifacts
make clean
```

## Documentation Structure

The guide is organized into the following chapters:

- **Preface**: Introduction and safety overview
- **System Overview**: Architecture and operating principles
- **Materials & Components**: Complete parts list and sourcing
- **Safety Guidelines**: Critical safety information
- **Chamber Construction**: Detailed fabrication instructions
- **Electrical System**: Power and control wiring
- **Control System**: Automation and monitoring
- **Testing & Calibration**: Commissioning procedures
- **Operation Manual**: Normal operation procedures
- **Troubleshooting**: Problem diagnosis and resolution  
- **Maintenance**: Preventive maintenance procedures
- **Appendix**: Technical references and resources

## Contributing

Contributions to improve the guide are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes to the appropriate `.adoc` files in `modules/ROOT/pages/`
4. Test the build locally
5. Submit a pull request

## License

This work is licensed under CC0 1.0 Universal. You are free to use, modify, and distribute this content without restriction.

## Safety Notice

⚠️ **IMPORTANT**: This project involves high voltages, high temperatures, and potentially hazardous chemicals. Always follow proper safety procedures and consult with qualified professionals before attempting construction.
