from player import PlayerDict

import json
from pathlib import Path

from ui import info


class PlayerStorage:
    def __init__(self, file: str | Path) -> None:
        self.file: Path = Path(file)
        self.file.parent.mkdir(parents=True, exist_ok=True)

        if not self.file.exists():
            self.file.write_text("{}", encoding="utf-8")

        self.data: dict[str, PlayerDict] = self.load()

    def load(self) -> dict[str, PlayerDict]:
        try:
            with self.file.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.decoder.JSONDecodeError) as e:
            info(f"Could not load player data ({e}), starting fresh.")
            info("File will be overwritten if you make a new player")
            return {}


    def update(self, data: dict[str, PlayerDict]) -> None:
        self.data.update(data)

    def save(self) -> None:
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def update_and_save(self, data: dict[str, PlayerDict]) -> None:
        self.update(data)
        self.save()