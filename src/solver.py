from typing import List

from src.types.info import Info, InfoType
from utils.helper_functions import calculate_info


class Solver:
    def __init__(self, word_list: List[str], word_dict: dict[str, int], word_length: int, total_word_freq: int,
                 current_info: List[Info],
                 not_present_letters: set[chr],
                 current_filtered_words: List[str]):
        self.word_list = word_list
        self.word_dict = word_dict
        self.word_length = word_length
        self.total_word_freq = total_word_freq
        self.current_info = current_info
        self.not_present_letters = not_present_letters
        self.current_filtered_words = current_filtered_words

    def insert_info(self, infos: List[Info]):
        for i, info in enumerate(infos):
            if self.current_info[i] == InfoType.CORRECT_PLACE:
                continue

            if info.info_type in (InfoType.CORRECT_PLACE, InfoType.WRONG_PLACE):
                self.current_info[i] = info
            elif info.info_type == InfoType.NOT_PRESENT:
                self.not_present_letters.add(info.letter)
            else:
                raise ValueError("Invalid InfoType")

    def get_guesses(self):
        filtered_words: dict[str, float] = {}

        current_info_known_letters_count: dict[chr, int] = {}
        for info in self.current_info:
            if info.info_type in (InfoType.CORRECT_PLACE, InfoType.WRONG_PLACE):
                if info.letter not in current_info_known_letters_count:
                    current_info_known_letters_count[info.letter] = 0
                current_info_known_letters_count[info.letter] += 1

        for word in self.current_filtered_words:
            if len(word) != self.word_length:
                continue
            if any(letter in self.not_present_letters for letter in word):
                continue
            # If letter that is present in correct place in current_info is not present in word, then skip
            if any(word[i] != info.letter for i, info in enumerate(self.current_info) if
                   info.info_type == InfoType.CORRECT_PLACE):
                continue

            freq_letters_dict: dict[chr, int] = {}
            for letter in word:
                if letter not in freq_letters_dict:
                    freq_letters_dict[letter] = 0
                freq_letters_dict[letter] += 1

            flag = True
            for letter, freq in freq_letters_dict.items():
                if letter in current_info_known_letters_count:
                    if freq > current_info_known_letters_count[letter]:
                        flag = False
                        break

            if flag:
                prob = (self.word_dict[word] / self.total_word_freq)
                filtered_words[word] = calculate_info(prob)

        return filtered_words
