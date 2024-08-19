import sys
from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.sendButton.clicked.connect(self.changeLabel)

    def changeLabel(self):
        text = self.lineEditName.text()
        self.label.setText(f"Hello, {text}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
