from enum import Enum


class FontItemSource(str, Enum):
    CUSTOM = "CUSTOM"
    GOOGLE = "GOOGLE"

    def __str__(self) -> str:
        return str(self.value)
