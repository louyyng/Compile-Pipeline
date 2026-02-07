# Automated C++ Compilation Pipeline (Multi-Arch)

This repository hosts a sophisticated CI/CD pipeline for C++ projects, featuring **matrix builds** and **automated release management**. It is designed to handle multi-architecture compilation (x64, x86) and automatic deployment upon tagging.

## Pipeline Workflow

The workflow (`.github/workflows/build.yml`) implements a professional DevOps cycle:

1.  **Parallel Execution**: Spawns multiple build runners for different platform configurations.
2.  **Compilation**: Uses MSBuild with dynamic parameters for `Configuration` and `Platform`.
3.  **Artifact Upload**: separating build outputs by architecture (`Build-x64-Release`, `Build-x86-Release`).
4.  **Release Trigger**: (Conditional) If a tag is detected, it downloads all artifacts, zips them, and publishes a formal GitHub Release.

## How to Use

### 1. Standard Development (CI)
Push code to `main` to verify builds across all architectures:
```bash
git add .
git commit -m "Refactor loader"
git push origin main
```
*Result: GitHub runs 2 parallel builds (x64, x86).*

### 2. Create a Release (CD)
To deploy a new version, simply tag your commit:
```bash
git tag v1.0
git push origin v1.0
```
*Result: GitHub builds the binaries and creates a "Release" page with the downloadable ZIP file.*

## Repository Structure

- `.github/workflows/build.yml`: The multi-stage CI/CD configuration.
- `*.sln`: Your Visual Studio solution file.
- `src/`: Source code.

---
*Disclaimer: This project is for educational and testing purposes only.*
