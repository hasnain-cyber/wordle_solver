from typing import List

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QScrollArea, QPushButton, QHBoxLayout, QLineEdit, \
    QFrame

from src.solver import Solver
from src.types.info import InfoType, Info
from src.types.state import State
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, word_dict: dict[str, int], total_word_freq: int):
        super().__init__()

        self.setWindowTitle("Wordle Solver")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.word_length = 5

        self.state = State(self.word_length)
        self.word_dict = word_dict
        self.total_word_freq = total_word_freq

        self.update_ui()

    def evaluate(self):
        for info in self.state.infos[-1]:
            if info.info_type == InfoType.NO_INFORMATION or not info.letter:
                return

        solver = Solver(self.word_dict, self.word_length, self.state.infos)
        guesses = solver.get_guesses()
        guesses.sort(key=lambda x: x[1], reverse=True)
        if len(guesses) <= 10:
            print(guesses)
        else:
            print(guesses[:10])

        self.state.infos.append([Info() for _ in range(self.word_length)])

        self.update_ui()

    def update_ui(self):
        rows_layout = QVBoxLayout()

        for i, info_state in enumerate(self.state.infos):
            rows_layout.addLayout(self.draw_row(info_state))

        rows_widget = QWidget()
        rows_widget.setLayout(rows_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidget(rows_widget)

        evaluate_button = QPushButton("Evaluate")
        evaluate_button.clicked.connect(self.evaluate)

        layout = QVBoxLayout()
        layout.addWidget(scroll_area)
        layout.addWidget(evaluate_button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def cycle_info_type(self, info):
        if info.letter:
            info_types: List[InfoType] = list(InfoType)
            current_index = info_types.index(info.info_type)
            next_index = (current_index + 1) % len(info_types)
            info.info_type = info_types[next_index]
        else:
            info.info_type = InfoType.NO_INFORMATION

        self.update_ui()

    def handle_text_change(self, text, info):
        if text:
            info.letter = text.lower()
        else:
            info.letter = ""
            info.info_type = InfoType.NO_INFORMATION

        self.update_ui()

    def draw_row(self, info_state: List[Info]) -> QHBoxLayout:
        row_layout = QHBoxLayout()

        for info in info_state:
            letter_layout = QVBoxLayout()

            line_edit = QLineEdit(info.letter if info.letter else "")
            line_edit.setFixedSize(40, 40)
            line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            line_edit.setMaxLength(2)
            line_edit.setStyleSheet(f"""
                                background-color: {info.info_type.color};
                                border: 1px solid black;
                                border-radius: 1px;
                            """)
            line_edit.textChanged.connect(
                lambda text, info_to_update=info: self.handle_text_change(text, info_to_update))
            letter_layout.addWidget(line_edit)

            box = QFrame()
            box.setFixedSize(40, 10)
            box.setStyleSheet(f"""
                        background-color: {info.info_type.color};
                        border: 1px solid black;
                        border-radius: 1px;
                    """)
            box.mousePressEvent = lambda event, info_to_cycle=info: self.cycle_info_type(info_to_cycle)
            letter_layout.addWidget(box)

            row_layout.addLayout(letter_layout)

        return row_layout
