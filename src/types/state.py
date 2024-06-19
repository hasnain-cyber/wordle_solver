from typing import List

from src.types.info import Info, InfoType


class State:
    def __init__(self, word_list: List[str], word_length: int):
        self.infos: List[List[Info]] = [[Info(InfoType.NO_INFORMATION, " ") for _ in range(word_length)]]
        self.not_present_letters: set[chr] = set()
        self.current_filtered_words: List[str] = word_list.copy()

    def add_info(self, info: List[Info]):
        self.infos.append(info)
