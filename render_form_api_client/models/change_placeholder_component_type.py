from enum import Enum


class ChangePlaceholderComponentType(str, Enum):
    CHART = "CHART"
    CIRCLE = "CIRCLE"
    HTML = "HTML"
    IMAGE = "IMAGE"
    QR_CODE = "QR_CODE"
    RATING = "RATING"
    RECTANGLE = "RECTANGLE"
    SVG_GROUP = "SVG_GROUP"
    TEST_OBJECT = "TEST_OBJECT"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
