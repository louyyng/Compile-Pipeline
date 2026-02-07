# Automated C++ Compilation Pipeline

This repository hosts a reusable GitHub Actions workflow for automatically compiling Windows C++ projects. It is designed to detect and build any Visual Studio Solution (`.sln`) found in the repository, making it easy to adapt for different projects (DLLs, EXEs, etc.).

## Workflow Steps

The pipeline (`.github/workflows/build.yml`) performs the following:

1.  **Checkout**: Retrieves the latest code from the repository.
2.  **Setup**: Installs the MSBuild toolchain on the runner.
3.  **Compile**: Builds the found solution in **Release** mode for **x64**.
4.  **Artifacts**: Collects all `.exe` and `.dll` files from the output directories and saves them as `Build-Artifacts`.

## How to Use

### 1. For This Project
Simply push your code changes. The pipeline will automatically rebuild the binaries.
```bash
git add .
git commit -m "Update code logic"
git push origin main
```
Go to the **Actions** tab in GitHub to monitor the build and download the resulting artifacts.

### 2. Reuse in Other Projects
To add this automated compilation to another C++ project:
1.  Copy the folder `.github/workflows/` to the root of your new project.
2.  Ensure your project has a valid `.sln` file.
3.  Push to GitHub.

## Repository Structure

- `.github/workflows/build.yml`: The CI/CD configuration file.
- `*.sln`: Your Visual Studio solution file.
- `src/` or equivalent: Your C++ source code files.

---
*Disclaimer: This project is for educational and testing purposes only.*