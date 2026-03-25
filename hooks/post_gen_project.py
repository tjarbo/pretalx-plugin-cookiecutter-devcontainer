import shutil
import subprocess
from pathlib import Path

if "github.com" not in "{{ cookiecutter.repo_url }}":
    shutil.rmtree(Path(".github"))

try:
    result = subprocess.run(["just", "fmt"], check=False)
    if result.returncode != 0:
        print(
            "\033[93m[warning]\033[0m \033[91m`just fmt` failed. This can be ignored, but please format the project manually and review the output.\033[0m"
        )
except Exception as exc:
    print(
        f"\033[93m[warning]\033[0m \033[91mCould not run `just fmt`: {exc}. This can be ignored, but please format the project manually.\033[0m"
    )
