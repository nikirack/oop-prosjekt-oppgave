from casino.app import Casino, select_player
from casino.games import Rps, Roulette
from casino.player import Player
from casino.storage import PlayerStorage
from casino.ui import info, clear

import time

"""
Selve filen som kjøres
Hånterer valg av spiller, og casino
"""

def main() -> None:

    storage = PlayerStorage("data/player.json")

    player: Player = select_player(storage)

    storage.update_and_save(player.to_dict())

    casino = Casino(
        storage=storage,
        player=player,
        games=[
            Rps(),
            Roulette(),
        ]
    )

    try:
        casino.run()
    except KeyboardInterrupt:
        info("\nBye")
        storage.update_and_save(player.to_dict())
        time.sleep(1.5)
        clear()



if __name__ == "__main__":
    main()
