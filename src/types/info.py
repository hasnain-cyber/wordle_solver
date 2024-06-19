from enum import Enum


class InfoType(Enum):
    CORRECT_PLACE = 1
    WRONG_PLACE = 2
    NOT_PRESENT = 3
    NO_INFORMATION = 4

    @property
    def color(self):
        return {
            InfoType.CORRECT_PLACE: "green",
            InfoType.WRONG_PLACE: "yellow",
            InfoType.NOT_PRESENT: "red",
            InfoType.NO_INFORMATION: "white"
        }[self]


class Info:
    def __init__(self, info_type: InfoType, letter: chr):
        self.info_type = info_type
        self.letter = letter
