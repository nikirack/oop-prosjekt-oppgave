from enum import Enum
from typing import TYPE_CHECKING

import pyfiglet
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.text import Text

if TYPE_CHECKING:
    from casino.games.shared.base import GameResult
    from casino.player import Player


"""
Dette er en fil for alt UI relatert, ingen andre filer snakker dirrekte med rich, de alle gjør det gjennom denne filen 
Denne filen er ganske AI generert
"""

class Color(Enum):
    ACCENT = "gold1"
    WIN = "bold green"
    LOSE = "bold red"
    DRAW = "bold yellow"
    INFO = "cyan"
    MUTED = "grey58"



console = Console()

def clear() -> None:
    # Clearing med ANSI escape koder
    print("\033[H\033[J", end="")

def titlecard(text: str) -> None:
    console.print(Panel(Align.center(pyfiglet.figlet_format(text))))

def fmt_credits(amount: int) -> str:
    return f"{amount:,} credits"

def show_player_balance(player: Player) -> None:
    console.print(f"Your credits: [{Color.ACCENT.value}]{fmt_credits(player.balance)}[/]")

def win(message: str) -> None:
    console.print(f"[{Color.WIN.value}]{message}[/]")

def lose(message: str) -> None:
    console.print(f"[{Color.LOSE.value}]{message}[/]")

def draw(message: str) -> None:
    console.print(f"[{Color.DRAW.value}]{message}[/]")

def info(message: str) -> None:
    console.print(f"[{Color.INFO.value}]{message}[/]")

def ask_int(prompt: str, choices: list[str] | None = None, show_choices: bool = True) -> int:
    if choices:
        return IntPrompt.ask(prompt, choices=choices, show_choices=show_choices)
    return IntPrompt.ask(prompt)

def ask_choice(prompt: str, choices: list[str], show_choices: bool = True) -> str:
    return Prompt.ask(prompt, choices=choices, show_choices=show_choices)

def print_result(result: GameResult) -> None:
    if result.outcome.value == "win":
        win(result.message)
    elif result.outcome.value == "loss":
        lose(result.message)
    else:
        draw(result.message)

def blank() -> None:
    console.print()

# En klasse for å lage menyene jeg bruker over hele prosjektet
class Menu:
    def __init__(self, title: str, options: dict[int, str], footer: str | None = None) -> None:
        self.title: str = title
        self.options: dict[int, str] = options
        self.footer: str | None = footer

    def ask(self) -> int:
        """Returns the key from the options dict (as an int)"""
        console.print(Text(self.title.upper(), style="bold"))
        blank()

        alternatives: list[str] = []

        for number, option in self.options.items():
            console.print(f"{number}. {option}")
            alternatives.append(str(number))

        if self.footer:
            alternatives.append("0")
            console.print(f"0. {self.footer}")

        return ask_int("", choices=alternatives, show_choices=False)



    def ask_option(self) -> str:
        """Returns the value from the options dict, not the key"""
        return self.options[self.ask()]
