from games import Dice
from player import Player
from casino import Casino, Startup
from storage import PlayerStorage

def main() -> None:

    storage = PlayerStorage("data/player.json")

    startup = Startup()

    player: Player = startup.select_player(storage)
    storage.update_and_save(player.to_dict())

    casino = Casino(
        storage=storage,
        player=player,
        games=[
            Dice(6),
        ]
    )

    casino.run()

if __name__ == "__main__":
    main()