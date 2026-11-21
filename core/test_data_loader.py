import json
from pathlib import Path


def load_test_data(filename: str) -> dict:
    path = Path(__file__).resolve().parent.parent / "test_data" / filename

    with path.open(encoding="utf-8") as file:
        return json.load(file)
