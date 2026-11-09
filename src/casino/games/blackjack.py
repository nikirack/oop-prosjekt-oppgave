from casino.games.shared.base import CasinoGame

class Blackjack(CasinoGame):
    def __init__(self) -> None:
        super().__init__("Blackjack", 10)

    