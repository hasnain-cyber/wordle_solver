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
            InfoType.NOT_PRESENT: "gray",
            InfoType.NO_INFORMATION: "white"
        }[self]

    def __repr__(self):
        return {
            InfoType.CORRECT_PLACE: "Correct Place",
            InfoType.WRONG_PLACE: "Wrong Place",
            InfoType.NOT_PRESENT: "Not Present",
            InfoType.NO_INFORMATION: "No Information"
        }[self]


class Info:
    def __init__(self, info_type: InfoType = InfoType.NO_INFORMATION, letter: chr = ''):
        self.info_type = info_type
        self.letter = letter

    def __repr__(self):
        return f"{self.info_type}: {self.letter}"
