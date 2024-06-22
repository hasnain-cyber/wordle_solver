from PySide6.QtWidgets import QApplication

from src.ui.main_window import MainWindow
from src.utils.loader.word_dict_loader import WordDictLoader
from src.utils.constants import WORDDICT_PATH


def main():
    word_dict_loader = WordDictLoader(WORDDICT_PATH)

    word_dict = word_dict_loader.get()
    total_word_freq = sum(word_dict.values())

    app = QApplication([])
    window = MainWindow(word_dict, total_word_freq)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
