<div align="center">

# RedForge

**Forge Your Red Team Workflow.**

A professional, open-source desktop workbench for penetration testers, bug bounty hunters, and red team operators.

[![Release](https://img.shields.io/badge/release-v0.1.0-EF4655?style=flat-square)](https://github.com/arpittoppo/RedForge/releases)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/UI-PySide6-41CD52?style=flat-square)](https://doc.qt.io/qtforpython/)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)]()

</div>

---

## What is RedForge?

RedForge is a **professional-grade desktop application** built for offensive security work. It replaces the scattered mess of Notion pages, spreadsheets, and markdown folders with a single, purpose-built workspace — one engagement at a time.

---

## v0.1.0 — What's Shipped

This is the first stable release of RedForge. The core engagement workflow is complete and functional.

### Launcher
- Engagement list with search and filter
- Recent engagements with quick-access context actions
- New Engagement dialog (name, target, type, VDP flag, description)
- Clean two-tier architecture: Launcher → per-engagement Workspace

### Workspace
Sidebar navigation split into logical groups:

**Core Modules**
| Module | Status |
|--------|--------|
| Dashboard | ✅ Live — engagement overview, severity summary, quick stats |
| Scope | ✅ Live — in-scope / out-of-scope target management |
| Recon | ✅ Live — recon entries with type tagging, status tracking, notes |
| Notes | ✅ Live — freeform markdown-style note-taking per engagement |
| Evidence | ✅ Live — evidence log with type classification and descriptions |
| Findings | ✅ Live — vulnerability findings with CRIT/HIGH/MED/LOW severity strips |
| Reports | ✅ Live — structured report generation per engagement |

### Infrastructure
- SQLite + SQLAlchemy persistence layer
- Per-engagement database isolation
- PyInstaller `.spec` for Windows executable builds
- GitHub Actions CI pipeline

---

## Installation

### From Release (Windows/linux)

Download the latest `.exe` installer from [Releases](https://github.com/arpittoppo/RedForge/releases) and run it. No Python required.

## Installation from Source

### Linux / macOS

```bash
git clone https://github.com/arpittoppo/RedForge.git
cd RedForge
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python -m redforge
```

### Windows

```powershell
git clone https://github.com/arpittoppo/RedForge.git
cd RedForge
python -m venv .venv
.venv\Scripts\activate
pip install -e .
python -m redforge
```

**Requirements:** Python 3.11+, PySide6, SQLAlchemy

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| UI Framework | PySide6 (Qt6) |
| Database | SQLite via SQLAlchemy |
| Packaging | PyInstaller |
| Linting | Ruff |
| Testing | pytest |

---
## Project Structure

```
RedForge/
├── src/
│   └── redforge/
│       ├── ui/
│       │   ├── pages/          # Dashboard, Scope, Recon, Notes, Evidence, Findings, Reports
│       │   ├── styles/         # theme.py, tokens.py
│       │   ├── assets/         # redforge.ico
│       │   └── widgets/        # Shared UI components
│       ├── models/             # SQLAlchemy models
│       └── core/               # Engagement logic
├── assets/                     # Project-level assets
├── docs/architecture/
├── installer/
├── RedForge.spec
└── pyproject.toml
```
## Contributing

RedForge is in active development. PRs, issues, and feature requests are welcome.

If you're a security professional with opinions on workflow — open an issue. This tool is built for people who do this work.

---

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

Built for the offensive security community. Use responsibly.

**[arpittoppo](https://github.com/arpittoppo)**

</div>
