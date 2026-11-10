from dataclasses import dataclass
from enum import Enum

from casino.ui import titlecard, info

# Enum for å tillate uavgjort
class GameOutcome(Enum):
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"

# En dataklasse som alle "CasinoGame" returner ved funksjonen play()
@dataclass
class GameResult:
    outcome: GameOutcome
    payout: int
    message: str


# Superklasse for alle casino spillene 
class CasinoGame:
    def __init__(self, name: str, min_bet: int = 10) -> None:
        self.name: str = name
        self.min_bet: int = min_bet

    def _show_title(self, bet: int) -> None:
        titlecard(self.name)
        info(f"Current bet is {bet}")

    def play(self, bet: int) -> GameResult:
        raise NotImplementedError