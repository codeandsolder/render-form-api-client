from enum import Enum


class RenderV2Output(str, Enum):
    IMAGE = "image"
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
