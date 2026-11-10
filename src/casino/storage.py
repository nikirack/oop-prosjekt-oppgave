from casino.player import PlayerDict

import json
from pathlib import Path

from casino.ui import info

# En klasse for å "snakke" med en json fil
class PlayerStorage:
    def __init__(self, file: str | Path) -> None:
        self.file: Path = Path(file)
        self.file.parent.mkdir(parents=True, exist_ok=True)

        if not self.file.exists():
            self.file.write_text("{}", encoding="utf-8")

        self.data: dict[str, PlayerDict] = self.load()

    # Henter dataen fra json filen
    def load(self) -> dict[str, PlayerDict]:
        try:
            with self.file.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.decoder.JSONDecodeError) as e: # Håntere feil vis noe har skjedd med json filen
            info(f"Could not load player data ({e}), starting fresh.")
            info("File will be overwritten if you make a new player")
            return {}

    # Oppdaterer dataen til en spiller som er i selve klassen (self.data) (dette endrer ikke på selve json filen)
    def update(self, data: dict[str, PlayerDict]) -> None:
        self.data.update(data)

    # Oppdaterer json filen og gjør at den er lik som self.data
    def save(self) -> None:
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def update_and_save(self, data: dict[str, PlayerDict]) -> None:
        self.update(data)
        self.save()