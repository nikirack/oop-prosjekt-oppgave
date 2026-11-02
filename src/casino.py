from player import Player, PlayerDict
from games.shared.base import CasinoGame, GameResult
from storage import PlayerStorage
from ui import clear, choose, prompt_int

import time

def _load_players(storage: PlayerStorage) -> Player:
    players: dict[str, PlayerDict] = storage.data
    players_numbered: dict[str, Player] = {}

    alternatives: set[str] = set()

    print("Select a player to use")


    for i, [uuid, player] in enumerate(players.items(), 1):
        player_class: Player = Player.from_dict(uuid, player)

        players_numbered[str(i)] = player_class
        print(f"{i}. {player_class.name} (Balance: {player_class.balance})")
        alternatives.add(str(i))
        
    choice: str = choose(alternatives)

    return players_numbered[choice]


def select_player(storage: PlayerStorage) -> Player:
    print("Select player")
    print("1. New player")

    alternatives: set[str] = {"1"}

    if bool(storage.load()):
        print("2. Load player")
        alternatives.add("2")

    choice: str = choose(alternatives)


    match choice:
        case "1":
            return Player(name = input("Name: "))
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
        print(f"Current balance: {self.player.balance}")
        print(f"Min bet is {game.min_bet}, write 0 to exit")

        bet: int = prompt_int("Bet: ")

        while bet != 0:
            if bet < game.min_bet:
                print(f"Minimum bet is {game.min_bet}.")
                bet = prompt_int("Bet: ")
            elif not self.player.has_amount(bet):
                print("You don't have enough credits.")
                bet = prompt_int("Bet: ")
            else:
                break


        if bet == 0:
            return
        
        self.player.change_balance(-bet)

        clear()
        print(f"---{game.name.upper()}---")
        print(f"Current bet is {bet}")

        result: GameResult = game.play(bet)
        self.player.change_balance(result.payout)

        print(result.message)
        print(f"{self.player.name} now has {self.player.balance} credits.")

        self.storage.update_and_save(self.player.to_dict())
        time.sleep(self.sleep_time)


    def select_game(self) -> None:
        clear()
        print("---GAMES---")

        alternatives: set[str] = {"0"}

        for num, game in self.games_numbered.items():
            print(f"{num}. {game.name}")
            alternatives.add(num)
            

        print("0. Back")

        
        choice: str = choose(alternatives)

        if choice == "0":
            return

        game: CasinoGame = self.games_numbered[choice]

        self.play_game(game)

            

    def run(self) -> None:
        while True:
            clear()
            print("---CASINO---")

            self.player.show_balance()
            print()

            print("1. Play")

            print("0. Exit")

            choice: str = choose({"1","0"})

            match choice:
                case "0":
                    print("Bye")
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