# datafun-02-project-setup
Utilities for scripting project folders

## Project Requirements

- VS Code
- Git
- Python 

## Professional Python Workflow

See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01/)

## Commands to Manage Virtual Environment

For Windows PowerShell (change if using Mac/Linux).
Verify that all required packages are included in requirements.txt (and have NOT been commented out).


```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

## Commands to Run Python Scripts

Remember to activate your .venv (and install packages if they haven't been installed yet) before running files.

TODO: Change these to reflect your Python file names and remove this TODO.

```shell
py utils_case.py
py dirbot_case.py
```

## Commands to Git add-commit-push

```shell
git add .
git commit -m "custom message"
git push -u origin main
```

## Reference Projects

Custom implementation of the example project at 
[datafun-02-project-setup](https://github.com/denisecase/datafun-02-project-setup)

- [Module 1 Repo](https://github.com/denisecase/datafun-01-utils/)
