from dataclasses import dataclass

from rich.panel import Panel
from rich.align import Align

from ui import console

@dataclass
class GameResult:
    win: bool
    payout: int
    message: str


class CasinoGame:
    def __init__(self, name: str, min_bet: int = 10) -> None:
        self.name: str = name
        self.min_bet: int = min_bet

    def _show_title(self, bet: int) -> None:
        console.print(Panel(Align.center(self.name.upper())))
        console.print(f"Current bet is {bet}")

    def play(self, bet: int) -> GameResult:
        raise NotImplementedError