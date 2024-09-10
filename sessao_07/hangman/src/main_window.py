import sys
import random
from constants import BIG_FONT_SIZE
from PySide6.QtCore import Qt
from window import Ui_MainWindow
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QApplication,
    QMessageBox,
    QSpacerItem,
    QSizePolicy,
    QLineEdit,
)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, words: list[str], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setupUi(self)
        self._word_list = words
        self._word = self._choice_word(words)
        self._setup_word()
        self.pushButton.clicked.connect(self._do_a_try)
        self.attempts = []

    def _choice_word(self, words):
        choiced_word = random.choice(words)
        self._guessed_word = ["*" if x != " " else " " for x in choiced_word]
        print(choiced_word)
        return choiced_word

    def _setup_word(self):
        self.statusbar.showMessage("Nenhuma tentativa")
        for index in range(len(self._word)):
            button = Field(self._word[index])
            if self._word[index] == " ":
                horizontalSpacer = QSpacerItem(
                    30, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
                )
                self.gridLayout.addItem(horizontalSpacer, 0, index)
                continue
            else:
                self.gridLayout.addWidget(button, 0, index)

    def _do_a_try(self):
        letters = self.letter_try.text().lower()
        for letter in letters:
            if letter in self.attempts:
                self._showError("Letra já tentada")
                continue
            self.attempts.append(letter)
            for row in range(self.gridLayout.rowCount()):
                for col in range(self.gridLayout.columnCount()):
                    item = self.gridLayout.itemAtPosition(row, col)
                    if item and isinstance(item.widget(), Field):
                        field = item.widget()
                        if isinstance(field, Field) and field.text().lower() == letter:
                            for i in range(len(self._word)):
                                if self._word[i] == letter:
                                    self._guessed_word[i] = letter
                            field.setProperty("cssClass", "visible")
                            field.style().unpolish(field)
                            field.style().polish(field)
        if "*" not in self._guessed_word:
            self._showInfo("Parabéns! Você venceu.")
        self.statusbar.showMessage(f"Tentativas: {' '.join(self.attempts)}")
        self.letter_try.clear()
        self.letter_try.setFocus()

    def makeMsgBox(self):
        return QMessageBox(self)

    def _makeDialog(self, text: str, icon: QMessageBox.Icon):
        msgBox = self.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(icon)
        return msgBox

    def _showInfo(self, text):
        msgBox = self._makeDialog(text, QMessageBox.Icon.Information)
        result = msgBox.exec()
        if result == QMessageBox.StandardButton.Ok:
            self._restart_game()

    def _restart_game(self):
        for row in range(self.gridLayout.rowCount()):
            for col in range(self.gridLayout.columnCount()):
                item = self.gridLayout.itemAtPosition(row, col)
                if item and isinstance(item.widget(), Field):
                    field = item.widget()
                    field.setProperty("cssClass", "hidden")
                    field.style().unpolish(field)
                    field.style().polish(field)
        self._word = self._choice_word(self._word_list)
        self._setup_word()
        self.attempts = []
        self.statusbar.showMessage("Nenhuma tentativa")
        self.letter_try.clear()
        self.letter_try.setFocus()

    def _showError(self, text):
        msgBox = self._makeDialog(text, QMessageBox.Icon.Critical)
        msgBox.exec()


class Field(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDisabled(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._config_style()
        self.setProperty("cssClass", "hidden")

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
    app = QApplication(sys.argv)
    mainWindow = MainWindow(words)
    qss = """QLineEdit[cssClass="hidden"] {
        background: transparent;
        color: transparent;
    }
    QLineEdit[cssClass="visible"] {
        color: black;
    }"""
    app.setStyleSheet(app.styleSheet() + qss)
    mainWindow.show()
    app.exec()
