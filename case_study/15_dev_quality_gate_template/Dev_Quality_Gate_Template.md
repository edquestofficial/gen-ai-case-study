# Dev Quality Gate Template 🚀

A lightweight yet powerful setup to automate code quality checks directly into your Git workflow. By integrating Pylint and Pytest Coverage into pre-commit and pre-push hooks, this template ensures that only clean, tested code makes it into your repository.
---

## High-Level Overview

```
          +--------------------------+
          |      Git Commit/Push     |
          +------------+-------------+
                       |
                       v
        +-------------------------------+
        |  Pre-commit Hook Triggered    |
        +-------------------------------+
                 |             |
        +--------+             +--------+
        |                             |
+-------------------+     +--------------------+
|  run_pylint.sh     |     |  run_coverage.sh   |
| (Pylint check)     |     | (Coverage check)   |
+-------------------+     +--------------------+
        |                             |
        v                             v
  Enforce Score + Lint         Enforce Coverage %
   Fail or Allow Commit        Fail or Allow Push
```

---

## Project Structure

```
dev-quality-gate-template/
├── scripts/
│   ├── run_pylint.sh         # Executes Pylint check with scoring & detailed output
│   └── run_coverage.sh       # Enforces test coverage threshold
├── .pre-commit-config.yaml   # Hooks setup for commit/push actions
├── requirements-dev.txt      # Dev dependencies (pylint, pytest, coverage, pre-commit)
├── sample_module/
│   └── sample_code.py        # Sample code module (Python logic to test quality gate)
├── tests/
│   └── test_sample.py        # Corresponding unit tests
├── README.md                 # Project documentation
└── pyproject.toml            # Configuration for tools like Pylint
```

---

##  Key Components

### Pylint Hook

**`scripts/run_pylint.sh`**

- Checks code against Pylint rules.
- Fails commit if:
  - Score is below a threshold (default: 8.0)
  - OR, if score is OK but issues exist, prints warnings but allows commit.

### Coverage Hook

**`scripts/run_coverage.sh`**

- Runs pytest with coverage.
- Fails push if coverage % is below required threshold.

### Pre-commit Config

**`.pre-commit-config.yaml`**

- Defines hooks for `pre-commit` and `pre-push` stages.
- Runs `run_pylint.sh` on commit.
- Runs `run_coverage.sh` on push.

---

## Tooling Breakdown

### Pylint
Static code analysis tool for Python.
- Enforces coding standards (e.g., PEP8).
- Identifies possible bugs, code smells, and style violations.
- Produces a score (0–10) indicating code quality.

### Pytest
Testing framework for Python.
- Supports simple unit tests to complex functional testing.
- Integrates well with fixtures, plugins, and mocking tools.

###  Coverage.py
Monitors test execution to report which lines of code were executed.
- Helps identify untested parts of code.
- Used with pytest via `pytest --cov` for seamless integration.

---

## ⚙️ Git Hooks Explained

### Pre-commit Hook
- Runs **before** a commit is finalized.
- Prevents bad code (e.g., failing lint checks) from being committed.
- In this project: Executes `run_pylint.sh` to check code quality.

### Pre-push Hook
- Runs **before** changes are pushed to a remote repository.
- Ensures all tests pass and code coverage requirements are met.
- In this project: Executes `run_coverage.sh` to enforce coverage threshold.

---

## Usage

### 1. Install dependencies

```bash
pip install -r requirements-dev.txt
```

### 2. Install hooks

```bash
pre-commit install --hook-type pre-commit
pre-commit install --hook-type pre-push
```

### 3. Try committing code

```bash
git add .
git commit -m "Check hooks"
```

---

## Benefits

- Automated enforcement of quality gates.
- Configurable thresholds for score and coverage.
- Works in any Python project.
- Avoids bad code reaching main branches.

---

## Perfect For

- Teams following CI/CD or GitFlow practices.
- Solo developers building high-quality packages.
- Open source projects looking for contribution standards.

---


