from player import Player, PlayerDict
from games.shared.base import CasinoGame, GameResult
from storage import PlayerStorage
from ui import clear, Menu, COLORS, fmt_credits, ask_int, info, print_result, titlecard, blank


def _load_players(storage: PlayerStorage) -> Player:

    clear()

    players: dict[str, PlayerDict] = storage.data
    players_numbered: dict[str, Player] = {}

    alternatives: dict[int, str] = {}


    for i, [uuid, player_dict] in enumerate(players.items(), 1):
        player: Player = Player.from_dict(uuid, player_dict)

        players_numbered[str(i)] = player
        alternatives[i] = f"{player.name} [{COLORS.muted.value}]{fmt_credits(player.balance)}[/]"

    menu = Menu(
        title="Select a player to use",
        options=alternatives
    )
     
    choice: str = menu.ask()

    return players_numbered[choice]


def select_player(storage: PlayerStorage) -> Player:
    clear()

    alternatives: dict[int, str] = {1:"New player"}

    if bool(storage.load()):
        alternatives[2] = "Load player"

    menu = Menu(
        title="Select player",
        options=alternatives,
    )

    choice: str = menu.ask()

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

        self.games_numbered: dict[int, CasinoGame] = {}
        for i, game in enumerate(self.games, 1):
            self.games_numbered[i] = game



    def play_game(self, game: CasinoGame) -> None:
        clear()

        self.player.show_balance()
        info(f"Min bet is {game.min_bet}, write 0 to exit")

        bet: int = ask_int("Bet")

        while bet != 0:
            if bet < game.min_bet:
                info(f"Minimum bet is {game.min_bet}.")
                bet = ask_int("Bet")
            elif not self.player.has_amount(bet):
                info("You don't have enough credits.")
                bet = ask_int("Bet")
            else:
                break


        if bet == 0:
            return
        
        self.player.change_balance(-bet)

        clear()

        result: GameResult = game.play(bet)
        self.player.change_balance(result.payout)

        print_result(result)
        info(f"{self.player.name} now has {fmt_credits(self.player.balance)}.")

        self.storage.update_and_save(self.player.to_dict())
        input("Press enter to continue")


    def select_game(self) -> None:
        clear()

        titlecard("GAMES")
        blank()

        alternatives: dict[int, str] = {}

        for num, game in self.games_numbered.items():
            alternatives[num] = game.name
            

        menu = Menu(
            title = "Select a game",
            options=alternatives
        )

        
        choice: str = menu.ask()

        if choice == "0":
            return

        game: CasinoGame = self.games_numbered[int(choice)]

        self.play_game(game)

            

    def run(self) -> None:
        while True:
            clear()

            titlecard("CASINO")

            self.player.show_balance()
            blank()

            menu = Menu(
                title="Select an option",
                options={
                    1: "Play"
                },
                footer="Exit"
            )

            choice: str = menu.ask()

            match choice:
                case "0":
                    info("Bye")
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