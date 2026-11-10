import random

from casino.games.shared.base import CasinoGame, GameResult

from casino.ui import Menu, info

"""
Stein saks papir
Lagt til for å ha et mindre komplisert spill en roulette
"""

class Rps(CasinoGame):
    WINNING: dict[str,str] = {
        "Rock": "Scissor",
        "Paper": "Rock",
        "Scissor": "Paper",
    }

    ALTERNATIVES: dict[int, str] = {
        1:"Rock",
        2:"Paper",
        3:"Scissor",
    }

    MENU = Menu(
            title="Rock, Paper, Scissor",
            options=ALTERNATIVES
        )

    def __init__(self) -> None:
        super().__init__("RPS", 10)

    def play(self, bet: int) -> GameResult:
        super()._show_title(bet)

        user_choice: str = self.MENU.ask_return_name()

        bot_choice: str = random.choice(list(self.ALTERNATIVES.values()))

        info(f"You chose {user_choice}, the bot chose {bot_choice}")

        if self.WINNING[user_choice] == bot_choice:
            return GameResult(True, bet * 2, f"You won {bet*2} credits!")
        elif user_choice == bot_choice:
            return GameResult(False, bet, f"Tie, your credits got returned!")
        else:
            return GameResult(False, 0, "You lost.")