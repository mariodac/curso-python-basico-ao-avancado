# QApplication e QPushButton de pySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.Widgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

button = QPushButton('Botão 1') 
button.setStyleSheet('font-size: 40px; color: red;')
button.show() # Adicionar o widget na hierarquia e exibe a janela

# button2 = QPushButton('Botão 2')
# button2.show()


app.exec() # O loop da aplicção