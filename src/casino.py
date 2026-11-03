from player import Player, PlayerDict
from games.shared.base import CasinoGame, GameResult
from storage import PlayerStorage
from ui import clear, console

from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt, IntPrompt

import time

def _load_players(storage: PlayerStorage) -> Player:

    clear()

    players: dict[str, PlayerDict] = storage.data
    players_numbered: dict[str, Player] = {}

    alternatives: list[str] = []

    table = Table()

    table.add_column("Number")
    table.add_column("Name")
    table.add_column("Balance")

    for i, [uuid, player] in enumerate(players.items(), 1):
        player_class: Player = Player.from_dict(uuid, player)

        players_numbered[str(i)] = player_class
        table.add_row(str(i), player_class.name, str(player_class.balance))

        alternatives.append(str(i))

    console.print(table)
     
    choice: str = Prompt.ask(
        "Select a player to use",
        choices=alternatives, 
        show_choices=False
    )

    return players_numbered[choice]


def select_player(storage: PlayerStorage) -> Player:
    clear()

    console.print("Select player")
    console.print("1. New player")

    alternatives: list[str] = ["1"]

    if bool(storage.load()):
        console.print("2. Load player")
        alternatives.append("2")

    choice: str = Prompt.ask(
        choices=alternatives
    )


    match choice:
        case "1":
            return Player(name = Prompt.ask("Name"))
        case "2":
            return _load_players(storage)
        case _:
            raise ValueError(f"Unexpected choice: {choice}") 


class Casino:
    def __init__(self, storage: PlayerStorage, player: Player, games: list[CasinoGame]) -> None:
        self.storage: PlayerStorage = storage
        self.player: Player = player
        self.games: list[CasinoGame] = games
        
        self.sleep_time = 1.5

        self.games_numbered: dict[str, CasinoGame] = {}
        for i, game in enumerate(self.games, 1):
            self.games_numbered[str(i)] = game



    def play_game(self, game: CasinoGame) -> None:
        clear()

        self.player.show_balance()
        console.print(f"Min bet is {game.min_bet}, write 0 to exit")

        bet: int = IntPrompt.ask("Bet")

        while bet != 0:
            if bet < game.min_bet:
                console.print(f"Minimum bet is {game.min_bet}.")
                bet = IntPrompt.ask("Bet")
            elif not self.player.has_amount(bet):
                console.print("You don't have enough credits.")
                bet = IntPrompt.ask("Bet")
            else:
                break


        if bet == 0:
            return
        
        self.player.change_balance(-bet)

        clear()

        result: GameResult = game.play(bet)
        self.player.change_balance(result.payout)

        console.print(result.message)
        console.print(f"{self.player.name} now has {self.player.balance} credits.")

        self.storage.update_and_save(self.player.to_dict())
        Prompt.ask("Press enter to continue")


    def select_game(self) -> None:
        clear()

        console.print(Panel(Align.center("GAMES")))
        console.print()

        alternatives: list[str] = ["0"]

        for num, game in self.games_numbered.items():
            console.print(f"{num}. {game.name}")
            alternatives.append(num)
            

        console.print("0. Back")

        
        choice: str = Prompt.ask(
            choices=alternatives,
            show_choices=False
        )

        if choice == "0":
            return

        game: CasinoGame = self.games_numbered[choice]

        self.play_game(game)

            

    def run(self) -> None:
        while True:
            clear()

            console.print(Panel(Align.center("CASINO")))

            self.player.show_balance()
            console.print()

            console.print("1. Play")

            console.print("0. Exit")

            choice: str = Prompt.ask(
                choices=["1","0"],
                show_choices=False
            )

            match choice:
                case "0":
                    console.print("Bye")
                    clear()
                    self.storage.update_and_save(self.player.to_dict())
                    return
                case "1":
                    self.select_game()
                case _:
                    pass
                    

# if __name__ == "__main__":
#     from games import Dice
#     play= Player("na")
#     ca = Casino(play,[Dice(6)])

#     ca.run()