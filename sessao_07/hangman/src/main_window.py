import sys
import random
from constants import BIG_FONT_SIZE
from PySide6.QtCore import Qt
from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QLineEdit


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, word: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        for letter in word:
            button = LineEdit(letter)
            self.horizontalLayout.addWidget(button)
            print(letter)


class LineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _config_style(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)


if __name__ == "__main__":
    themes = {}
    words = [
        "python",
        "programação",
        "desenvolvimento",
        "computador",
        "curso",
        "ciencia de dados",
        "inteligencia artificial",
    ]
    choiced_word = random.choice(words)
    app = QApplication(sys.argv)
    mainWindow = MainWindow(choiced_word)
    mainWindow.show()
    app.exec()
