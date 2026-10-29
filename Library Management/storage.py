import json
from pathlib import Path
from typing import Any


class JSONStorage:
    """Handle saving and loading data from JSON files."""

    # LOGIC 1: Initialize the JSON file path.
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)

        # LOGIC 2: Load data from the JSON file.
    def load_data(self) -> Any:
        # Return an empty list if the file does not exist.
        if not self.file_path.exists():
            return []

        # Read and return the saved JSON data.
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"Invalid JSON data in {self.file_path}"
            ) from error

            # LOGIC 3: Save data to the JSON file.
    def save_data(self, data: Any) -> None:
        # Create the parent folder if it does not exist.
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the data in JSON format.
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

