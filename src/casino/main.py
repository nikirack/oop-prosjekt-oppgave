from casino.app import Casino, select_player
from casino.games import Dice, Roulette
from casino.player import Player
from casino.storage import PlayerStorage

def main() -> None:

    storage = PlayerStorage("data/player.json")

    player: Player = select_player(storage)

    storage.update_and_save(player.to_dict())

    casino = Casino(
        storage=storage,
        player=player,
        games=[
            Dice(6),
            Roulette(),
        ]
    )

    casino.run()

if __name__ == "__main__":
    main()
