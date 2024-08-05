from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from constants import MEDIUM_FONT_SIZE 
from utils import isNumOrDot, isEmpty, isValidNumber
from typing import TYPE_CHECKING
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
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)   

        self._gridMask = [
            ['\u2102', '\u25C0', '^', '/'],
            ['7', '8', '9', '*'],
            ['6', '5', '4', '-'],
            ['3', '2', '1', '+'],
            ['0', '.', '=', '']
        ]
        self.display = display
        self.info = info
        self._equation = ''
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
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                if isEmpty(buttonText):
                    continue
                if buttonText == '0':
                    self.addWidget(button, i, j, 1, 2)
                    index = j + 1
                elif index is not None and j >= index:
                    self.addWidget(button, i, j+1)
                else:
                    self.addWidget(button, i, j)
            
                buttonSlot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, buttonSlot)

    def _connectButtonClicked(self, button:Button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button:Button):
        text = button.text()
        if text == '\u2102':
            # buttonSlot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, self._clear)
            

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
        self.equation = ''
        