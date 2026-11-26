# Git Branching Strategy

- `main`: stable, reviewed project code.
- `feature/monitor`: website checking logic.
- `feature/dashboard`: dashboard interface and results display.

Workflow:
1. Create a feature branch from `main`.
2. Make changes and commit with clear messages.
3. Run tests locally.
4. Push the feature branch to GitHub.
5. Open a Pull Request into `main`.
6. Review and merge after checks pass.

Example commands:
```bash
git switch -c feature/monitor
git add .
git commit -m "Add website monitoring feature"
git push -u origin feature/monitor
```
