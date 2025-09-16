# GitHub Pages Deployment Guide

This document provides information about the GitHub Pages deployment setup for the MOERC documentation site.

## Overview

The MOERC documentation is built using [Antora](https://antora.org/) and automatically deployed to GitHub Pages using GitHub Actions.

## Deployment Workflow

### Automatic Deployment

The deployment happens automatically when:
- Code is pushed to the `main` branch
- The workflow can also be triggered manually from the Actions tab

### Workflow Steps

1. **Checkout**: Repository code is checked out
2. **Setup Node.js**: Node.js 18 is installed with npm caching
3. **Install Dependencies**: `npm ci` installs project dependencies
4. **Build Site**: `npm run build:site` builds the Antora documentation
5. **Upload Artifact**: The built site (`build/site/`) is uploaded as a Pages artifact
6. **Deploy**: The artifact is deployed to GitHub Pages

## Configuration

### Repository Settings

For the workflow to work properly, ensure that:

1. **GitHub Pages is enabled** in repository settings
2. **Source is set to "GitHub Actions"** (not "Deploy from a branch")
3. **Workflow permissions** allow writing to Pages (handled by the workflow configuration)

### Workflow File

The workflow is defined in `.github/workflows/deploy-pages.yml` and includes:
- Proper permissions for Pages deployment
- Concurrency control to prevent deployment conflicts
- Error handling and artifact uploading

## Manual Deployment

To manually trigger a deployment:

1. Go to the repository's **Actions** tab
2. Select the **"Deploy to GitHub Pages"** workflow
3. Click **"Run workflow"**
4. Select the **main** branch
5. Click **"Run workflow"** button

## Troubleshooting

### Common Issues

1. **Build Failures**: Check the Actions logs for npm install or build errors
2. **Permission Errors**: Ensure Pages permissions are properly configured
3. **Missing Files**: Verify that `build/site/` contains the expected files after build

### Local Testing

Before pushing changes, test the build locally:

```bash
# Clean previous builds
npm run clean

# Install dependencies
npm ci

# Build the site
npm run build:site

# Preview locally
npm run preview
```

Visit http://localhost:8080 to preview the site.

## Site URL

The deployed site is available at: https://pierce403.github.io/moerc

## Maintenance

- The workflow uses the latest stable versions of GitHub Actions
- Node.js version is pinned to 18 for consistency
- Dependencies are cached to improve build performance
- The workflow includes concurrency controls to prevent deployment conflicts