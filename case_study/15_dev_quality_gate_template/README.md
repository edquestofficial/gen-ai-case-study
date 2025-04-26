# dev-quality-gate-template

This project enforces quality gates on Git operations using Git hooks.

## Features
- Pylint score must be >= 8.0
- Code coverage must be >= 80%
- Uses pre-commit framework

## Setup
```bash
pip install -r requirements-dev.txt
pre-commit install --hook-type pre-push
```

## Usage
Make code changes and try to push. The push will be blocked if quality gates fail.

---

Add your own code in `sample_module/` and tests in `tests/`.






















🧵 Twitter Thread Format
1/ 🚨 Want to catch bad code before it hits your main branch?
Here’s a mini framework to enforce code quality gates using pylint, pytest, and coverage—right in your Git workflow! 🔥

2/ 📂 Project Structure

bash
Copy
Edit
dev-quality-gate-template/
├── scripts/
│   ├── run_pylint.sh
│   └── run_coverage.sh
├── .pre-commit-config.yaml
├── sample_module/
├── tests/
3/ ✅ What it does:

Fails commit if linting fails or score too low.

Fails push if test coverage is below threshold.

Works using Git pre-commit & pre-push hooks!


4/ 🛠 Tools used:

pylint: checks coding standards & gives score.

pytest: runs your test suite.

coverage.py: checks test coverage.

pre-commit: handles Git hooks like a champ.


5/ ⚙️ Example Hook Behavior

Bad naming? Function too long? ➡️ 🔥 Hook blocks commit.

Score < 8.0? ➡️ 🔥 Hook blocks commit.

Coverage < 80%? ➡️ 🔥 Hook blocks push.

6/ 📦 Easy setup:

bash
Copy
Edit
pip install -r requirements-dev.txt
pre-commit install --hook-type pre-commit
pre-commit install --hook-type pre-push
7/ 🤯 Pro tip: You can customize score threshold, coverage %, and more! This template is 🔁 reusable for any Python project!

8/ 📈 Raise your team’s code quality game today 💯
#Python #DevTools #PreCommit #CleanCode #GitHooks

============================================



📸 Instagram Carousel Format
Slide 1:
🛡️ Enforce Code Quality Before You Commit
🔧 With Pylint + Pytest + Git Hooks
#PythonDev #CodeQuality

Slide 2:
🧰 Tools Used
✔️ pylint – code analysis + scoring
✔️ pytest – testing framework
✔️ coverage – test coverage
✔️ pre-commit – Git hook runner

Slide 3:
💥 What Gets Blocked?
❌ Linting issues
❌ Pylint score < 8.0
❌ Test coverage < 80%
✅ Otherwise, you’re good to go!

Slide 4:
⚙️ Git Hook Flow

git commit → triggers run_pylint.sh

git push → triggers run_coverage.sh
All automated 🧠

Slide 5:
📦 Project Folder Layout Quick, clean, modular
(Side-by-side diagram image)

Slide 6:
🚀 Perfect for:
✅ Solo Devs
✅ Open Source Maintainers
✅ CI/CD Teams

Slide 7:
🔗 Install and Go!

bash
Copy
Edit
pip install -r requirements-dev.txt  
pre-commit install --hook-type pre-commit  
pre-commit install --hook-type pre-push
Slide 8:
🧵 Want the full walkthrough?
Check out the repo + save this post!
#PythonTips #DeveloperTools #GitHooks #CleanCode
