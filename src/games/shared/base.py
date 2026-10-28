from player import Player

class CasinoGame:
    def __init__(self, name: str, min_bet: int = 10) -> None:
        self.name: str = name
        self.min_bet: int = min_bet

    def is_valid_bet(self, bet:int, player:Player) -> bool:
        if type(bet) != int:
            return False

        if bet < self.min_bet:
            return False

        if bet > player.balance:
            return False

        return True

    def play(self, player: Player, bet: int) -> tuple[bool, str]:
        if not self.is_valid_bet(bet, player):
            return False, "Invalid bet"

        player.change_balance(-bet)

        return True, "Bet accepted"
 