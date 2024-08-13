from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from constants import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from utils import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Delete, KEYS.Key_Backspace]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus,
            KEYS.Key_Minus,
            KEYS.Key_Slash,
            KEYS.Key_Asterisk,
            KEYS.Key_AsciiCircum,
        ]

        if isEnter or text == "=":
            self.eqPressed.emit()
            # print(f"enter pressionado evento emitido em {self.__class__}")
            return event.ignore()

        if isDelete:
            # print("delete pressionado")
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            # print("esc pressionado")
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            self.operatorPressed.emit(text)
            # print("operator press", text)
            return event.ignore()

        # se remover o retorno do evento desabilita todas as outras teclas
        # return super().keyPressEvent(event)
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            # print("inputpress pressionado")
            self.inputPressed.emit(text)
            return event.ignore()

        # print(f"Texto {text}")
