from typing import TypedDict

import uuid


class PlayerDict(TypedDict):
    name: str
    balance: int

class Player:
    def __init__(self, name:str, balance:int=1000) -> None:
        self.name: str = name
        self.balance: int = balance
        
        self.uuid: uuid.UUID = uuid.uuid4()

    def change_balance(self, amount:int) -> None:
        self.balance += amount

    def show_balance(self) -> None:
        print(f"{self.name} has {self.balance} credits.")

    def has_amount(self, amount:int) -> bool:
        return self.balance >= amount
    
    def to_dict(self) -> dict[str, PlayerDict]:
        return {str(self.uuid):{"name": self.name, "balance": self.balance}}

    @classmethod
    def from_dict(cls, uuid_key: str, data: PlayerDict) -> "Player":
        player = cls(data["name"], data["balance"])

        player.uuid = uuid.UUID(uuid_key)
        return player
