import random
from typing import ClassVar

from casino.games.shared.base import CasinoGame
from casino.games.shared.results import GameOutcome, GameResult
from casino.ui import Menu, info

"""
Stein saks papir
Lagt til for å ha et mindre komplisert spill en roulette
"""

class RPS(CasinoGame):
    BEATS: ClassVar[dict[str, str]] = {
        "Rock": "Scissor",
        "Paper": "Rock",
        "Scissor": "Paper",
    }

    CHOICES: ClassVar[dict[int, str]] = {
        1:"Rock",
        2:"Paper",
        3:"Scissor",
    }

    def __init__(self) -> None:
        super().__init__("RPS", 10)

    def play(self, bet: int) -> GameResult:
        super()._show_title(bet)

        menu: Menu = Menu(
            title="Rock, Paper, Scissor",
            options=self.CHOICES
        )
        user_choice: str = menu.ask_option()

        bot_choice: str = random.choice(list(self.CHOICES.values()))

        info(f"You chose {user_choice}, the bot chose {bot_choice}")

        if self.BEATS[user_choice] == bot_choice:
            return GameResult(GameOutcome.WIN, bet * 2, f"You won {bet*2} credits!")
        elif user_choice == bot_choice:
            return GameResult(GameOutcome.DRAW, bet, "Tie, your credits got returned!")
        else:
            return GameResult(GameOutcome.LOSS, 0, "You lost.")