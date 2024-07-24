import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
from math import sqrt

class Calculator(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Minha Calculadora")
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #A0A0A0; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1, style='background: #0790E2; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''), 'background: #FF5733; color: #fff; font-weight: 700;')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1, style='background: #0790E2; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]), 'background: #FF5733; color: #fff; font-weight: 700;')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1, style='background: #0790E2; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('\u221A'), 3, 4, 1, 1, self.eval_sqrt, 'background: #0790E2; color: #fff; font-weight: 700;') 

        self.add_btn(QPushButton('0'), 4, 0, 1, 1)
        self.add_btn(QPushButton('.'), 4, 1, 1, 1)
        self.add_btn(QPushButton('='), 4, 2, 1, 1, self.eval_equal, 'background: #06E758; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1, style='background: #0790E2; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('x²'), 4, 4, 1, 1, lambda: self.display.setText(
            str(
                round(float(self.display.text())**2, 2)
    
            )
        ), style='background: #0790E2; color: #fff; font-weight:700;')

        self.setCentralWidget(self.cw)

    def eval_sqrt(self):
        try:
            self.display.setText(str(round(sqrt(float(self.display.text())), 2)))
        except:
            self.display.setText('Conta inválida')

    def eval_equal(self):
        try:
            # eval() é uma função que avalia a expressão especificada; se a expressão for uma instrução Python válida, ela será executada.
            self.display.setText(str(round(float(eval(self.display.text())), 2)))
        except:
            self.display.setText('Conta inválida')

    def add_btn(self, btn:QWidget, row:int, col:int, rowspan:int, colspan:int, function = None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not function:
            btn.clicked.connect(
                lambda: self.display.setText(self.display.text() + btn.text())
            )
        else:
            btn.clicked.connect(function)
        if style:
            btn.setStyleSheet(style)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()