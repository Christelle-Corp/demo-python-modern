# Demo Python Modern - GHAS Testing

**⚠️ WARNING: This repository contains intentionally vulnerable dependencies for security scanning demonstration purposes.**

## Purpose

This repository demonstrates GitHub Advanced Security (GHAS) Dependabot capabilities for Python projects using both modern (UV) and traditional (pip) package managers.

## Vulnerable Dependencies

This project includes the following known vulnerabilities:

- **Django 2.2.0** - Multiple CVEs including SQL injection and XSS vulnerabilities
- **Flask 0.12.2** - CVE-2018-1000656 (Denial of service)
- **requests 2.6.0** - CVE-2015-2296 (Cookie handling)
- **PyYAML 5.1** - CVE-2020-1747 (Arbitrary code execution)
- **Jinja2 2.10.0** - CVE-2019-10906 (Sandbox escape)

## Package Manager Support

This repository demonstrates dual package manager support:

### UV (Modern)
- `pyproject.toml` - Project metadata and dependencies
- `uv.lock` - Lock file with exact versions and integrity hashes

### pip (Traditional Fallback)
- `requirements.txt` - Pinned dependencies for pip compatibility

## Expected GHAS Behavior

When Dependabot is enabled, it should:
- Detect vulnerable dependencies from both `pyproject.toml` and `requirements.txt`
- Create security alerts for each CVE
- Optionally create automated PRs with version bumps
- Handle both UV and pip package manager formats

## Running the Application (Not Recommended)

```bash
# Using pip
pip install -r requirements.txt
python src/app.py

# Using UV
uv sync
python src/app.py

# Access at http://localhost:5000
```

## DO NOT USE IN PRODUCTION

This code is for demonstration purposes only and should never be deployed to production environments.
