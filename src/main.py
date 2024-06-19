from PySide6.QtWidgets import QApplication

from src.ui.main_window import MainWindow
from src.utils.loader.word_dict_loader import WordDictLoader
from src.utils.loader.word_list_loader import WordlistLoader
from src.utils.constants import WORDLIST_PATH, WORDDICT_PATH


def main():
    word_list_loader = WordlistLoader(WORDLIST_PATH)
    word_dict_loader = WordDictLoader(WORDDICT_PATH)

    word_list = word_list_loader.get()
    word_dict = word_dict_loader.get()
    total_word_freq = word_dict_loader.get_total_freq()

    app = QApplication([])
    window = MainWindow(word_list, word_dict, total_word_freq)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
