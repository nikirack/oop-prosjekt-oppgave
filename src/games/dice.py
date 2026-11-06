import random

from games.shared.base import CasinoGame, GameResult

from ui import ask_int

class Dice(CasinoGame):
    def __init__(self, sides:int) -> None:
        super().__init__("Dice", 10)
        self.sides: int = sides
        self.multiplier = 2

    def play(self, bet: int) -> GameResult:
        super()._show_title(bet)

        user_side: int = ask_int(
            f"Choose a side from 1 to {self.sides}", 
            choices=[str(i) for i in range(1, self.sides+1)]
        )


        number: int = random.randint(1, self.sides)

        if number == user_side:
            return GameResult(True, bet*self.multiplier, f"You won {bet*self.multiplier} credits!")
        
        return GameResult(False, 0, "You lost.")