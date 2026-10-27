import random

class Player:
    def __init__(self, name:str, balance:int=1000) -> None:
        self.name: str = name
        self.balance: int = balance

    def change_balance(self, amount:int) -> None:
        self.balance += amount

    def show_balance(self) -> None:
        print(f"{self.name} har {self.balance}.")


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

