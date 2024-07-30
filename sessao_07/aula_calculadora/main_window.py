from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Calculadora")


    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())