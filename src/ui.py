import subprocess, platform
from rich.console import Console

console = Console()

def clear() -> None:
    subprocess.run(
        ["cls"] if platform.system() == "Windows" else ["clear"],
        check=False,
        shell=True
    )
