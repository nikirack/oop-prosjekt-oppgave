from abc import ABC, abstractmethod

from casino.games.shared.results import GameResult
from casino.ui import info, titlecard


# Superklasse for alle casino spillene 
class CasinoGame(ABC):
    def __init__(self, name: str, min_bet: int = 10) -> None:
        self.name: str = name
        self.min_bet: int = min_bet

    def _show_title(self, bet: int) -> None:
        titlecard(self.name)
        info(f"Current bet is {bet}")
    
    @abstractmethod
    def play(self, bet: int) -> GameResult:
        "Selve funksjonen der casino spillet skal eksistere"