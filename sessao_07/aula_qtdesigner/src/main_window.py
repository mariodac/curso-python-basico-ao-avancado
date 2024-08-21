import sys

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from typing import cast


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.sendButton.clicked.connect(self.changeLabel)

        self.lineEditName.installEventFilter(self)

    def changeLabel(self):
        text = self.lineEditName.text()
        self.label.setText(f"Hello, {text}!")

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineEditName.text()
            self.label.setText(text + event.text())
        return super().eventFilter(watched, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
