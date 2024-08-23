import sys
import random
from constants import BIG_FONT_SIZE
from PySide6.QtCore import Qt
from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QLineEdit


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, word: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setupUi(self)
        # self.setFixedSize(self.width(), self.height())
        print(word)
        for index in range(len(word)):
            button = LineEdit(word[index])
            if word[index] == " ":
                continue
            else:
                self.gridLayout.addWidget(button, 1, index)


class LineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDisabled(True)
        self._config_style()

    def _config_style(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setGeometry(221, 9, 91, 95)


if __name__ == "__main__":
    themes = {}
    words = [
        "python",
        "programacao",
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
