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
    QLineEdit,
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
            button = Field(word[index])
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
        letters = self.letter_try.text().lower()
        for letter in letters:
            for row in range(self.gridLayout.rowCount()):
                for col in range(self.gridLayout.columnCount()):
                    item = self.gridLayout.itemAtPosition(row, col)
                    if item and isinstance(item.widget(), Field):
                        field = item.widget()
                        if isinstance(field, Field) and field.text().lower() == letter:
                            field.setProperty("cssClass", "visible")
                            field.style().unpolish(field)
                            field.style().polish(field)
        self.letter_try.clear()


class Field(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDisabled(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._config_style()
        self.setProperty("cssClass", "invisible")

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
    print(choiced_word)
    app = QApplication(sys.argv)
    mainWindow = MainWindow(choiced_word)
    qss = """
    QLineEdit[cssClass="invisible"] {{
        background: transparent;
        color: transparent;
    }}
    QLineEdit[cssClass="visible"] {{
        color: black;
    }}
    """
    app.setStyleSheet(app.styleSheet() + qss)
    mainWindow.show()
    app.exec()
