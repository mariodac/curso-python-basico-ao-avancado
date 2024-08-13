from PySide6.QtWidgets import QPushButton, QGridLayout, QMessageBox
from PySide6.QtCore import Slot
from constants import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber
from typing import TYPE_CHECKING
from math import pow

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
        self, display: "Display", info: "Info", window: "MainWindow", *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["\u2102", "\u25C0", "^", "/"],
            ["7", "8", "9", "*"],
            ["6", "5", "4", "-"],
            ["3", "2", "1", "+"],
            ["0", ".", "=", "+/-"],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ""
        self.equationInitValue = "Sua conta"
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self.equationInitValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.eqPressed.connect(self._equal)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)
        index = None
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)
                if isEmpty(buttonText):
                    continue
                # ignora o ultimo botão
                # if buttonText == "0":
                #     self.addWidget(button, i, j, 1, 2)
                #     index = j + 1
                if index is not None and j >= index:
                    self.addWidget(button, i, j + 1)
                else:
                    self.addWidget(button, i, j)

                buttonSlot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, buttonSlot)

    def _connectButtonClicked(self, button: Button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: Button):
        text = button.text()
        if text == "\u2102":
            # buttonSlot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, self._clear)

        if text == "\u25C0":
            self._connectButtonClicked(button, self.display.backspace)

        if text in "+-/*^":
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOp, button.text())
            )

        if text == "+/-":
            self._connectButtonClicked(button, self._invertNumberSignal)

        if text == "=":
            self._connectButtonClicked(button, self._equal)

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    @Slot()
    def _invertNumberSignal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        newNumber = convertToNumber(displayText) * -1

        self.display.setText(str(newNumber))

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text
        if isValidNumber(newDisplayValue):
            self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self.display.clear()
        self.equation = self.equationInitValue
        self._left = None
        self._right = None
        self._operator = None
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()  # deverá ser meu numero _left
        self.display.clear()

        # se a pessoa clicou no operador sem configurar qualquer numero
        if not isValidNumber(displayText) and self._left is None:
            self._showWarning("Você não digitou nada")
            return

        # se houver algo no número da esquerda, não fazemos nada
        # aguardaremos o número da direita
        if self._left is None:
            self._left = convertToNumber(displayText)

        self._operator = text
        self.equation = f"{self._left} {self._operator} ??"
        self.display.setFocus()

    def _equal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError("Conta incompleta")
            return

        self._right = convertToNumber(displayText)
        self.equation = f"{self._left} {self._operator} {self._right}"
        result = "error"
        try:
            # verificar variaveis com varias instancias isinstance(self._left, int | float) ou isinstance(self._left, (int, float))
            if "^" in self.equation and isinstance(self._left, int | float):
                result = pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self.display.clear()
            self.info.setText(f"Operação inválida {self.equation}")
            self._showError("Voce está divindo por zero")
        except OverflowError:
            self.display.clear()
            self.info.setText(f"Excedeu os limites do float")
            self._showError("Esta conta não pode ser realizado")

        self.display.clear()
        result = convertToNumber(str(result))
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None

        if result == "error":
            self._left = None
        self.display.setFocus()

    def _makeDialog(self, text: str, icon: QMessageBox.Icon):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(icon)
        return msgBox

    def _showWarning(self, text):
        msgBox = self._makeDialog(text, QMessageBox.Icon.Warning)
        # msgBox.setInformativeText(
        #     "Est laboris culpa nisi elit incididunt cupidatat excepteur."
        # )
        # adicionar mais de um botão
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Ok
        #     | msgBox.StandardButton.Cancel
        #     | msgBox.StandardButton.Save
        # )
        # alterar texto do botão padrão
        # QTranslator Class para traduzir texto
        # msgBox.button(msgBox.StandardButton.Ok).setText("Certo")
        # obter qual botão o usuario clicou
        result = msgBox.exec()

        # if result == msgBox.StandardButton.Save:
        #     print(f"{text} - Salvar")
        # elif result == msgBox.StandardButton.Cancel:
        #     print(f"{text} - Cancelar")
        # else:
        #     print(f"{text} - Ok")
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text, QMessageBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()

    def _showError(self, text):
        msgBox = self._makeDialog(text, QMessageBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
