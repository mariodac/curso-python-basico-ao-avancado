"""
PyQT é um tootlkit desenvolvido em C++ utilizado por vários programas para 
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede, etc
pip install pyqt5
docs: https://www.riverbankcomputing.com/static/Docs/PyQt5/
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QGridLayout

class App(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Eu sou um botão')
        self.btn.setStyleSheet('font-size: 30px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.action)
        # self.btn.clicked.connect(lambda: print("Olá mundo!"))

        self.setCentralWidget(self.cw)

    def action(self):
        print('Ação realizada')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
