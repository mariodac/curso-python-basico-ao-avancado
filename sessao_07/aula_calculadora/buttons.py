from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from constants import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from typing import TYPE_CHECKING
from math import pow

if TYPE_CHECKING:
    from display import Display
    from info import Info


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
    def __init__(self, display: "Display", info: "Info", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["\u2102", "\u25C0", "^", "/"],
            ["7", "8", "9", "*"],
            ["6", "5", "4", "-"],
            ["3", "2", "1", "+"],
            ["0", ".", "=", ""],
        ]
        self.display = display
        self.info = info
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
        index = None
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)
                if isEmpty(buttonText):
                    continue
                if buttonText == "0":
                    self.addWidget(button, i, j, 1, 2)
                    index = j + 1
                elif index is not None and j >= index:
                    self.addWidget(button, i, j + 1)
                else:
                    self.addWidget(button, i, j)

                buttonSlot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, buttonSlot)

    def _connectButtonClicked(self, button: Button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: Button):
        text = button.text()
        if text == "\u2102":
            # buttonSlot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, self._clear)

        if text in "+-/*^":
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button)
            )

        if text in "=":
            self._connectButtonClicked(button, self._equal)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, button: Button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        if isValidNumber(newDisplayValue):
            self.display.insert(buttonText)

    def _clear(self):
        self.display.clear()
        self.equation = self.equationInitValue
        self._left = None
        self._right = None
        self._operator = None

    def _operatorClicked(self, button):
        buttoText = button.text()  # operadores (+-/*)
        displayText = self.display.text()  # deverá ser meu numero _left
        self.display.clear()

        # se a pessoa clicou no operador sem configurar qualquer numero
        if not isValidNumber(displayText) and self._left is None:
            return

        # se houver algo no número da esquerda, não fazemos nada
        # aguardaremos o número da direita
        if self._left is None:
            self._left = float(displayText)

        self._operator = buttoText
        self.equation = f"{self._left} {self._operator} ??"

    def _equal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        self._right = float(displayText)
        self.equation = f"{self._left} {self._operator} {self._right}"
        result = "error"
        try:
            if "^" in self.equation and isinstance(self._left, float):
                result = pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self.display.clear()
            self.info.setText(f"Operação inválida {self.equation}")
        except OverflowError:
            self.display.clear()
            self.info.setText(f"Excedeu os limites do float")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None

        if result == "error":
            self._left = None
