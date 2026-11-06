from games.shared.base import CasinoGame, GameResult

import random

from ui import ask_choice

class Roulette(CasinoGame):
    def __init__(self) -> None:
        super().__init__("Roulette", 10)
        
        self.multiplier = 2
        self.alternatives: list[str] = ["Red", "Black"]

    def play(self, bet: int) -> GameResult:
        super()._show_title(bet)

        ball: str = random.choice(self.alternatives)
        user_guess: str = ask_choice(
            "Place your bet",
            choices=self.alternatives,
        )

        if ball == user_guess:
            return GameResult(True, bet * self.multiplier, f"You won {bet*self.multiplier} credits!")
        
        return GameResult(False, 0, "You lost.")