class Player:
    def __init__(self, name:str, balance:int=1000) -> None:
        self.name: str = name
        self.balance: int = balance

    def change_balance(self, amount:int) -> None:
        self.balance += amount

    def show_balance(self) -> None:
        print(f"{self.name} har {self.balance}.")

    def has_amount(self, amount:int) -> bool:
        return self.balance >= amount