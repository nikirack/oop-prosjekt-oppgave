import random

from games.shared.base import CasinoGame
from player import Player


class Dice(CasinoGame):
    def __init__(self, sides:int) -> None:
        super().__init__("Dice", 10)
        self.sides: int = sides
        self.multiplier = 2

    def play(self, player:Player, bet:int) -> tuple[bool, str]:
        success, status = super().play(player, bet)

        if not success:
            return False, status

        while True:
            try:
                user_side = int(
                    input(f"Choose a side from 1 to {self.sides}: ")
                )

                if 1 <= user_side <= self.sides:
                    break

                print(f"Please choose a number between 1 and {self.sides}.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

        number: int = random.randint(1, self.sides)

        if number == user_side:
            player.change_balance(bet * self.multiplier)
            return True, "Player won"
        
        return True, "Player lost"