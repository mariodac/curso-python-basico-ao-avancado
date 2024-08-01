import sys
from constants import WINDOW_ICON_PATH
from main_window import MainWindow
from display import Display
from buttons import Button, ButtonsGrid
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit
from styles import setupTheme

if __name__ == "__main__":
    # Cria aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Info initialization
    info = Info('2.0 ^ 10.0 = 1024.0')
    window.addWidgetToVLayout(info)

    # Display initialization
    display = Display()
    display.setPlaceholderText('Digite um numero')
    window.addWidgetToVLayout(display)

    # Grid layout
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)
    
    # Button initialization
    # buttonsGrid.addWidget(Button('0'), 0, 0)
    # buttonsGrid.addWidget(Button('1'), 0, 1)
    # buttonsGrid.addWidget(Button('2'), 0, 2)
    # buttonsGrid.addWidget(Button('3'), 1, 2)

    # define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))  
    window.setWindowIcon(icon)
    # app.setWindowIcon(icon)
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    window.adjustFixedSize()
    window.show()
    app.exec()