from games.shared.base import CasinoGame, GameResult

import random
from enum import Enum

from ui import ask_int, info, Menu

class RouletteColor(Enum):
    Red = "Red"
    Black = "Black"
    Green = "Green"

class Roulette(CasinoGame):
    # Faktiske rulette tall, https://www.wikihow.com/Play-Roulette
    RED_NUMBERS: list[int] = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    BLACK_NUMBERS: list[int] = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    GREEN_NUMBERS: list[int] = [0]

    ALL_NUMBERS: list[int] = sorted([*RED_NUMBERS, *BLACK_NUMBERS, *GREEN_NUMBERS])

    BET_TYPES: dict[int, str] = {
        1:"Number",
        2:"Red",
        3:"Black",
        4:"Even",
        5:"Odd",
        6:"1-18",
        7:"19-36",
        8:"1st dozen",
        9:"2nd dozen",
        10:"3rd dozen"
    }

    MULTIPLIERS: dict[str, int] = {
        "Number": 36,
        "Red": 2, "Black": 2,
        "Even": 2, "Odd": 2,
        "1-18": 2, "19-36": 2,
        "1st dozen": 3, "2nd dozen": 3, "3rd dozen": 3,
    }

    def __init__(self) -> None:
        super().__init__("Roulette", 10)

    def _spin(self) -> tuple[int, RouletteColor]:
        number: int = random.choice(self.ALL_NUMBERS)

        if number in self.GREEN_NUMBERS:
            return (number, RouletteColor.Green)
        elif number in self.RED_NUMBERS:
            return (number, RouletteColor.Red)
        else:
            return (number, RouletteColor.Black)
        

    def _wins(self, choice: str, pick: int, ball: tuple[int, RouletteColor]) -> bool:
        number, color = ball

        if number == 0:
            return choice == "Number" and pick == 0

        match choice:
            case "Number":
                return number == pick
            case "Red" | "Black":
                return color.value == choice
            case "Even":
                return number % 2 == 0
            case "Odd":
                return number % 2 == 1
            case "1-18":
                return 1 <= number <= 18
            case "19-36":
                return 19 <= number <= 36
            case "1st dozen":
                return 1 <= number <= 12
            case "2st dozen":
                return 13 <= number <= 24
            case "3st dozen":
                return 25 <= number <= 36
            case _:
                raise ValueError(f"Unexpected choice: {choice}") 

    def play(self, bet: int) -> GameResult:
        super()._show_title(bet)

        menu = Menu(
            title = "Select a bet",
            options=self.BET_TYPES
        )

        choice: str = menu.ask_return_name()

        pick: int = 0
        if choice == "Number":
            pick = ask_int("Pick a number (0-36)", choices=[str(i) for i in self.ALL_NUMBERS])

        ball: tuple[int, RouletteColor] = self._spin()
        info(f"The ball lands on {ball[0]} {ball[1].value}.")

        if self._wins(choice, pick, ball):
            payout: int = bet * self.MULTIPLIERS[choice]
            return GameResult(True, payout, f"{choice} wins! You won {payout} credits!")

        return GameResult(False, 0, f"{choice} loses. You lost.")
