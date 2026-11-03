from games.shared.base import CasinoGame, GameResult
# from ui import console

import random

from rich.prompt import Prompt

class Roulette(CasinoGame):
    def __init__(self) -> None:
        super().__init__("Roulette", 10)
        
        self.multiplier = 2
        self.alternatives: list[str] = ["Red", "Black"]

    def play(self, bet: int) -> GameResult:
        super()._show_title(bet)

        ball = random.choice(self.alternatives)
        user_guess = Prompt.ask(
            "Place your bet",
            choices=self.alternatives
        )

        if ball == user_guess:
            return GameResult(True, bet * self.multiplier, f"You won {bet*self.multiplier} credits!")
        
        return GameResult(False, 0, "You lost.")