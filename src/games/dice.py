import random

from games.shared.base import CasinoGame, GameResult
from ui import prompt_int


class Dice(CasinoGame):
    def __init__(self, sides:int) -> None:
        super().__init__("Dice", 10)
        self.sides: int = sides
        self.multiplier = 2

    def play(self, bet: int) -> GameResult:
        while True:
            user_side: int = prompt_int(f"Choose a side from 1 to {self.sides}: ")

            if 1 <= user_side <= self.sides:
                break

            print(f"Please choose a number between 1 and {self.sides}.")


        number: int = random.randint(1, self.sides)

        if number == user_side:
            return GameResult(True, bet*self.multiplier, f"You won {bet*self.multiplier} credits!")
        
        return GameResult(False, 0, "You lost.")