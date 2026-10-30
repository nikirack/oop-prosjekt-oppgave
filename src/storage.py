from player import PlayerDict

import json
from pathlib import Path


class PlayerStorage:
    def __init__(self, file: str | Path) -> None:
        self.file: Path = Path(file)
        self.file.parent.mkdir(parents=True, exist_ok=True)

        if not self.file.exists():
            self.file.write_text("{}", encoding="utf-8")

        self.data: dict[str, PlayerDict] = self.load()

    def load(self) -> dict[str, PlayerDict]:
        with self.file.open("r", encoding="utf-8") as f:
            return json.load(f)

    def update(self, data: dict[str, PlayerDict]) -> None:
        self.data.update(data)

    def save(self) -> None:
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def update_and_save(self, data: dict[str, PlayerDict]) -> None:
        self.update(data)
        self.save()