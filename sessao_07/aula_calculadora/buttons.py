from PySide6.QtWidgets import QPushButton, QGridLayout
from constants import MEDIUM_FONT_SIZE 
from utils import isNumOrDot, isEmpty

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   

        self._gridMask = [
            ['\u2102', '\u25C0', '^', '/'],
            ['7', '8', '9', '*'],
            ['6', '5', '4', '-'],
            ['3', '2', '1', '+'],
            ['0', '.', '=', '']
        ]
        self._makeGrid()

    def _makeGrid(self):
        index = None
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                if isEmpty(buttonText):
                    continue
                if buttonText == '0':
                    self.addWidget(button, i, j, 1, 2)
                    index = j + 1
                elif index is not None and j >= index:
                    self.addWidget(button, i, j+1)
                else:
                    print('Linha', i, 'coluna', j, buttonText)
                    self.addWidget(button, i, j)
        