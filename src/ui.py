import subprocess, platform

def clear() -> None:
    subprocess.run(
        ["cls"] if platform.system() == "Windows" else ["clear"],
        check=False,
        shell=True
    )


def choose(valid: set[str], msg: str = "Choose: ", error: str = "You need to choose a valid alternative") -> str:
    while True:
        choice: str = input(msg)

        if choice in valid:
            return choice
        
        print(error)


def prompt_int(msg: str) -> int:
    while True:
        try:
            choice = int(input(msg))
            return choice
        except ValueError:
            print("You need to write a whole number")