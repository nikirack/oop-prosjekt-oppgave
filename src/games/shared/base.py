from dataclasses import dataclass

from ui import titlecard, info

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
        titlecard(self.name)
        info(f"Current bet is {bet}")

    def play(self, bet: int) -> GameResult:
        raise NotImplementedError