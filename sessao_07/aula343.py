# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#      -> CentralWidget (centrla_widget)
#           -> Layout (layout)
#               -> Widget 1 (button1)
#               -> Widget 2 (button2)
#              -> Widget 3 (button3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

def slot_example(status_bar):
    status_bar.showMessage('Hello world!')

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Janelinha')

button1 = QPushButton('Botão 1') 
button1.setStyleSheet('font-size: 40px; color: red;')

button2 = QPushButton('Botão 2')
button2.setStyleSheet('font-size: 60px;')

button3 = QPushButton('Botão 3')
button3.setStyleSheet('font-size: 80px; color: green;')

layout = QGridLayout() # Layout com linha e coluna personalizado
central_widget.setLayout(layout)
# para adicionar em layout em grid
layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem de status')

# menuBar
menu = window.menuBar()
first_menu = menu.addMenu('Primeiro Menu')
first_action = first_menu.addAction('Primeira ação')
first_action.triggered.connect(lambda: slot_example(status_bar))



window.show() # qmainwindow entre na hierarquia e mostre sua janela

app.exec() # O loop da aplicção