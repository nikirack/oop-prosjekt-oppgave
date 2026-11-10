from typing import TYPE_CHECKING, Optional
from enum import Enum

from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

import pyfiglet

if TYPE_CHECKING:
    from casino.player import Player
    from casino.games.shared.base import GameResult


"""
Dette er en fil for alt UI relatert, ingen andre filer snakker dirrekte med rich, de alle gjør det gjennom denne filen 
Denne filen er ganske AI generert
"""

class COLORS(Enum):
    accent = "gold1"
    win = "bold green"
    lose = "bold red"
    info = "cyan"
    muted = "grey58"



console = Console()

def clear() -> None:
    # Clearing med ANSI escape koder
    print("\033[H\033[J", end="")

def titlecard(text: str) -> None:
    console.print(Panel(Align.center(pyfiglet.figlet_format(text))))

def fmt_credits(amount: int) -> str:
    return f"{amount:,} credits"

def show_player_balance(player: Player) -> None:
    console.print(f"Your credits: [{COLORS.accent.value}]{fmt_credits(player.balance)}[/]")

def win(message: str) -> None:
    console.print(f"[{COLORS.win.value}]{message}[/]")

def lose(message: str) -> None:
    console.print(f"[{COLORS.lose.value}]{message}[/]")

def info(message: str) -> None:
    console.print(f"[{COLORS.info.value}]{message}[/]")

def ask_int(prompt: str, choices: Optional[list[str]] = None, show_choices: bool = True) -> int:
    if choices:
        return IntPrompt.ask(prompt, choices=choices, show_choices=show_choices)
    return IntPrompt.ask(prompt)

def ask_choice(prompt: str, choices: list[str], show_choices: bool = True) -> str:
    return Prompt.ask(prompt, choices=choices, show_choices=show_choices)

def print_result(result: GameResult) -> None:
    if result.win:
        win(result.message)
    else:
        lose(result.message)

def blank() -> None:
    console.print()

# En klasse for å lage menyene jeg bruker over hele prosjektet
class Menu:
    def __init__(self, title: str, options: dict[int, str], footer: Optional[str] = None) -> None:
        self.title: str = title
        self.options: dict[int, str] = options
        self.footer: Optional[str] = footer

    def ask(self) -> str:
        console.print(Text(self.title.upper(), style="bold"))
        blank()

        alternatives: list[str] = []

        for number, option in self.options.items():
            console.print(f"{number}. {option}")
            alternatives.append(str(number))

        if self.footer:
            alternatives.append("0")
            console.print(f"0. {self.footer}")

        return ask_choice("", alternatives, show_choices=False)



    def ask_return_name(self) -> str:
        return self.options[int(self.ask())]