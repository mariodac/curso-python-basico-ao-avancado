# O básico sobre Signal e Slots (eventos e documentação)

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
from  PySide6.QtGui import QAction
from PySide6.QtCore import Slot

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton('Botão 1') 
        self.button.setStyleSheet('font-size: 40px; color: red;')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Janelinha')

        self.button1 = self.make_button('Botão 1')
        self.button1.clicked.connect(self.second_action_checked )

        self.button2 = self.make_button('Botão 2')

        self.button3 = self.make_button('Botão 3')

        self.grid_layout = QGridLayout() # Layout com linha e coluna personalizado
        self.central_widget.setLayout(self.grid_layout)
        # para adicionar em layout em grid
        self.grid_layout.addWidget(self.button1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mensagem de status')

        # menuBar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Primeiro Menu')
        self.first_action = self.first_menu.addAction('Primeira ação')
        # first_action.triggered.connect(lambda: slot_example(status_bar))
        self.first_action.triggered.connect(self.change_status_message)

        self.second_action = self.first_menu.addAction('Segunda ação')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_action_checked)
        self.second_action.hovered.connect(self.second_action_checked)


        

    @Slot()
    def change_status_message(self):
        self.status_bar.showMessage('Hello world!')

    @Slot()
    def second_action_checked(self):
        if self.second_action.isChecked():
            print('Marcado')
        else:
            print('Desmarcado')

    def make_button(self, text_btn):
        btn = QPushButton(text_btn) 
        btn.setStyleSheet('font-size: 40px; color: red;')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show() # qmainwindow entre na hierarquia e mostre sua janela

    app.exec() # O loop da aplicção