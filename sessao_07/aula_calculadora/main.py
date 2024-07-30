import sys
from constants import WINDOW_ICON_PATH
from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit

if __name__ == "__main__":
    # Cria aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Info initialization
    info = Info('2.0 ^ 10.0 = 1024.0')
    window.addWidgetToVLayout(info)

    # Display initialization
    display = Display()
    display.setPlaceholderText('Digite um numero')
    window.addWidgetToVLayout(display)

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