# 🛡️ AI Action Firewall

> **Security middleware for AI agents — evaluate, control, and audit agent actions before they reach business systems.**

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-0A9EDC)](https://pytest.org/)
[![Lint](https://img.shields.io/badge/Lint-Ruff-D7FF64)](https://docs.astral.sh/ruff/)
[![Status](https://img.shields.io/badge/Status-MVP%20Development-orange)](#project-status)

## 🎯 Overview

AI Action Firewall is a production-oriented security layer between an AI agent and the tools/APIs it wants to use. It evaluates requested actions against identity, permissions, policies and risk signals before deciding whether the action should be **allowed, monitored, approved or blocked**.

## ✨ Core Capabilities

- 🔐 AI-agent action authorization
- 🧩 Policy-based enforcement
- 🧠 ML-assisted risk scoring
- 🚦 Allow / monitor / approval / block decisions
- 📝 Security event and audit logging
- 📊 Security visibility dashboard
- 🔌 API-first architecture
- 🧪 Automated testing
- ⚙️ Environment-based configuration

## 🏗️ Architecture

```text
AI Agent → Action Request → AI Action Firewall
                              ├─ Identity & Access
                              ├─ Policy Evaluation
                              ├─ Risk Analysis
                              └─ Audit Logging
                                      │
                              ┌───────┴───────┐
                              ▼               ▼
                           ALLOW/BYPASS     BLOCK/REVIEW
                              │
                              ▼
                       Business Tool/API
```

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python + FastAPI |
| Packaging | uv + pyproject.toml |
| ML | Python ML stack / risk models |
| Frontend | Web application |
| Database | PostgreSQL target |
| Cache | Redis target |
| Containers | Docker target |
| CI/CD | GitHub Actions target |
| API Docs | OpenAPI / FastAPI |

## 📁 Repository Structure

```text
ai-action-firewall/
├── backend/       # FastAPI application and business logic
├── frontend/      # Web dashboard
├── ml/            # Risk-scoring and ML components
├── tests/         # Automated tests
├── docs/          # Architecture and product documentation
├── scripts/       # Developer/operations scripts
├── .env.example   # Environment configuration template
├── pyproject.toml
├── PRODUCT_DEFINITION.md
└── README.md
```

## 🚀 Quick Start

```bash
git clone https://github.com/aizaz512/ai-action-firewall.git
cd ai-action-firewall
uv sync
uv run uvicorn backend.app.main:app --reload
```

Run tests and linting:

```bash
uv run pytest
uv run ruff check backend tests
```

## 📚 Documentation

- [Product Definition](PRODUCT_DEFINITION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Case Study](docs/CASE_STUDY.md)
- [Demo Script](docs/DEMO_SCRIPT.md)

## 📌 Project Status

**Early MVP development.** The project is being built incrementally from a working FastAPI foundation toward a production-ready AI security SaaS. Features are marked complete only after implementation and testing.

### Roadmap

- [x] FastAPI backend foundation
- [x] Application configuration
- [ ] Authentication and authorization
- [ ] Agent/action request schema
- [ ] Policy engine
- [ ] Allow/block workflow
- [ ] Audit event storage
- [ ] ML risk scoring
- [ ] Dashboard
- [ ] PostgreSQL integration
- [ ] Docker deployment
- [ ] CI/CD pipeline
- [ ] Cloud deployment
- [ ] Usage metering and billing
- [ ] Public SaaS launch

## 💼 Portfolio Value

This repository demonstrates product thinking, backend architecture, security controls, testing, documentation and a roadmap from MVP to SaaS.

## 👤 Author

**Aizaz Ur Rahman** — Python Developer & AI/ML Engineer

[GitHub](https://github.com/aizaz512) · [Repositories](https://github.com/aizaz512?tab=repositories)

---

⭐ If you find the project interesting, consider starring the repository.
