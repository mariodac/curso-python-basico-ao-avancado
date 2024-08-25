import sys
import random
from constants import BIG_FONT_SIZE
from PySide6.QtCore import Qt
from window import Ui_MainWindow
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QApplication,
    QPushButton,
    QSpacerItem,
    QSizePolicy,
)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, word: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setupUi(self)
        self._setup_word(word)
        print(word)
        self.pushButton.clicked.connect(self._word_list)

    def _setup_word(self, word: str):
        self.buttons = []
        for index in range(len(word)):
            button = Button(word[index])
            # id = word.index(word[-1])
            # if index == id:
            #     button.setProperty("cssClass", "visible")
            if word[index] == " ":
                horizontalSpacer = QSpacerItem(
                    30, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
                )
                self.gridLayout.addItem(horizontalSpacer, 0, index)
                continue
            else:
                self.gridLayout.addWidget(button, 0, index)
            self.buttons.append(button)

    def _word_list(self):
        letters = self.letter_try.text()
        item = self.gridLayout.itemAt(0).widget()
        item.setProperty("cssClass", "invisible")
        item.setParent(self)
        print(item)


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDisabled(True)
        self._config_style()
        self.setProperty("cssClass", "invisibles")

    def _config_style(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)


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
        "algoritmo",
        "estrutura de dados",
        "logica de programacao",
        "programacao orientada a objetos",
        "software livre",
    ]
    choiced_word = random.choice(words)
    app = QApplication(sys.argv)
    mainWindow = MainWindow(choiced_word)
    mainWindow.show()
    qss = """
    QPushButton[cssClass="invisible"] {
        background: #FFFFFF;
        color: #FFFFFF
        }
    """
    app.setStyleSheet(app.styleSheet() + qss)
    app.exec()
