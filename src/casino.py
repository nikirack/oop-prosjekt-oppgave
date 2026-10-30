from player import Player, PlayerDict
from games.shared.base import CasinoGame
from storage import PlayerStorage

import time
import subprocess
import platform

class Startup:
    def __init__(self) -> None:
        pass

    def _load_players(self, storage: PlayerStorage):
        players: dict[str, PlayerDict] = storage.data
        players_numbered: dict[str, Player] = {}

        print("Select a player to use")

        for i, [uuid, player] in enumerate(players.items(), 1):
            player_class: Player = Player.from_dict(uuid, player)

            players_numbered[str(i)] = player_class
            print(f"{i}. {player_class.name} (Balance: {player_class.balance})")

        while True:
            choice: str = input("Choose: ")

            try:
                return_player: Player = players_numbered[choice]
                return return_player
            except KeyError:
                print("You need to choose a player")

    def select_player(self, storage: PlayerStorage) -> Player:
        print("Select player")
        print("1. New player")
        print("2. Load player")

        while True:
            choice = input("Choose: ")

            match choice:
                case "1":
                    return Player(name = input("Name: "))
                case "2":
                    return self._load_players(storage)
                case _:
                    print("Select a valid choice")
                


class Casino:
    def __init__(self, storage: PlayerStorage, player: Player, games: list[CasinoGame]) -> None:
        self.storage: PlayerStorage = storage
        self.player: Player = player
        self.games: list[CasinoGame] = games
        
        self.sleep_time = 1.5

        self.games_numbered: dict[str, CasinoGame] = {}
        for i, game in enumerate(self.games, 1):
            self.games_numbered[str(i)] = game


    def clear(self) -> None:
        subprocess.run(
            ["cls"] if platform.system() == "Windows" else ["clear"],
            check=False,
            shell=True
        )

    def play_game(self, game: CasinoGame):
        print(f"Current balance: {self.player.balance}")
        print(f"Min bet is {game.min_bet}, write 0 to exit")
        while True:
            try:
                bet = int(input("Bet: "))
                break
            except ValueError:
                print("Bet needs to be a number")

        if bet == 0:
            return

        self.clear()

        print(f"---{game.name.upper()}---")
        print(f"Current bet is {bet}")

        _status, message = game.play(self.player, bet)

        print(message)
        self.storage.update_and_save(self.player.to_dict())
        time.sleep(self.sleep_time)


    def select_game(self):
        self.clear()
        print("---GAMES---")

        for num, game in self.games_numbered.items():
            print(f"{num}. {game.name}")

        print("0. Back")

        try:
            choice = input("choose: ")

            if choice == "0":
                return

            game: CasinoGame = self.games_numbered[choice]

            self.play_game(game)

        except KeyError:
            print("You need to choose a game")
            time.sleep(self.sleep_time)

            

    def run(self) -> None:
        while True:
            self.clear()
            print("---CASINO---")

            self.player.show_balance()
            print()

            print("1. Play")

            print("0. Exit")

            choice = input("choose: ")

            match choice:
                case "0":
                    print("Bye")
                    self.storage.update_and_save(self.player.to_dict())
                    return
                case "1":
                    self.select_game()

                case _:
                    print("\nNot a choice")
                    time.sleep(self.sleep_time)
                    

# if __name__ == "__main__":
#     from games import Dice
#     play= Player("na")
#     ca = Casino(play,[Dice(6)])

#     ca.run()