from typing import List

from src.types.info import Info, InfoType
from utils.helper_functions import calculate_info


class Solver:
    def __init__(self, word_dict: dict[str, int], word_length: int,
                 current_info: List[List[Info]]):
        self.word_dict = word_dict
        self.word_length = word_length
        self.current_info = current_info

    def get_guesses(self):
        total_word_freq = sum(self.word_dict.values())

        filtered_words = []

        not_present_letters = set()
        for info_list in self.current_info:
            for info in info_list:
                if info.info_type == InfoType.NOT_PRESENT:
                    not_present_letters.add(info.letter)

        for info_list in self.current_info:
            for info in info_list:
                if (info.info_type in (
                        InfoType.CORRECT_PLACE, InfoType.WRONG_PLACE)) and info.letter in not_present_letters:
                    not_present_letters.remove(info.letter)

        for word, freq in self.word_dict.items():
            if len(word) != self.word_length:
                continue
            if any(letter in not_present_letters for letter in word):
                continue
            # If letter that is present in correct place in current_info is not present in word, then skip
            flag = True
            for info_list in self.current_info:
                for i, info in enumerate(info_list):
                    if info.info_type == InfoType.CORRECT_PLACE and word[i] != info.letter:
                        flag = False
                        break

            if not flag:
                continue

            prob = (freq / total_word_freq)
            filtered_words.append((word, prob))

        return filtered_words
