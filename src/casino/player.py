import uuid
from typing import TypedDict

from casino.games.shared.results import GameOutcome
from casino.ui import show_player_balance


# En TypedDict som korelerer med hvordan dataen er strukturert i json filen
class PlayerDict(TypedDict):
    name: str
    balance: int
    stats: Statistics

class Statistics(TypedDict):
    win: int
    loss: int
    draw: int

# En klasse for spilleren
class Player:
    def __init__(self, name:str, balance:int=1000) -> None:
        self.name: str = name
        self.balance: int = balance
        self.stats: Statistics = {
            "win":0,
            "loss":0,
            "draw":0
        }

        # UUID for å ha forskjellige keys i json filen   
        self.uuid: uuid.UUID = uuid.uuid4()

    def update_stats(self, result: GameOutcome) -> None:
        self.stats[result.value] += 1

    def change_balance(self, amount:int) -> None:
        self.balance += amount

    def show_balance(self) -> None:
        show_player_balance(self)

    def has_amount(self, amount:int) -> bool:
        return self.balance >= amount

    # En metode for å returnere dataen til spilleren på en måte som gjør at vi kan lagre det
    def to_dict(self) -> dict[str, PlayerDict]:
        return {str(self.uuid):{"name": self.name, "balance": self.balance, "stats": self.stats}}

    # En "classmethod" som gjør at vi kan lage en spiller fra et dict, det motsatte av "to_dict" metoden
    @classmethod
    def from_dict(cls, uuid_key: str, data: PlayerDict) -> Player:
        player = cls(data["name"])
        player.balance = data["balance"]
        player.stats = data["stats"]

        player.uuid = uuid.UUID(uuid_key)
        return player
