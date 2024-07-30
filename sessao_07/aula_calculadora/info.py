from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from constants import SMALL_FONT_SIZE, MINIMUM_WIDTH

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size:{SMALL_FONT_SIZE}')
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)