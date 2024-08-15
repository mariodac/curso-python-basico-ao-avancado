from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        # Configurando o layout básico
        self.centralW = QWidget()
        self.vLayout = QVBoxLayout()
        self.centralW.setLayout(self.vLayout)
        self.setCentralWidget(self.centralW)

        # Titulo da janela
        self.setWindowTitle("Calculadora")

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
