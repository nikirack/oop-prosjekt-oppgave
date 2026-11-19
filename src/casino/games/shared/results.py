from dataclasses import dataclass
from enum import Enum


# Enum for å tillate uavgjort
class GameOutcome(Enum):
    "Enum from result"
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"

# En dataklasse som alle "CasinoGame" returner ved funksjonen play()
@dataclass
class GameResult:
    outcome: GameOutcome
    payout: int
    message: str