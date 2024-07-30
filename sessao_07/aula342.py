# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Botão 1') 
button.setStyleSheet('font-size: 40px; color: red;')

button2 = QPushButton('Botão 2')
button2.setStyleSheet('font-size: 60px;')

button3 = QPushButton('Botão 3')
button3.setStyleSheet('font-size: 80px; color: green;')

central_widget = QWidget()
# layout = QHBoxLayout() # Layout na horizontal
# layout = QVBoxLayout()  # Layout na vertical
layout = QGridLayout() # Layout com linha e coluna personalizado
central_widget.setLayout(layout)
# para adicionar em layout horizontal e vertical
# layout.addWidget(button)
# layout.addWidget(button2)
# para adicionar em layout em grid
layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

central_widget.show() # Central widget entre na hierarquia e mostre sua janela

app.exec() # O loop da aplicção