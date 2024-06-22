from typing import List

from src.types.info import Info


class State:
    def __init__(self, word_length: int):
        self.infos: List[List[Info]] = [[Info() for _ in range(word_length)]]
