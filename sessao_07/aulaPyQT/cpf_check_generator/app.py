from PyQt5.QtCore import Qt
from validator_cpf import validate_cpf
from generator_cpf import generate_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QGuiApplication
from pathlib import Path
import design
import sys
import re


ROOT_FOLDER = Path(__file__).parent
ICON_WINDOW_PATH = ROOT_FOLDER / 'accuracy.png'
print(ICON_WINDOW_PATH)

class CpfCheckGenerator(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        self.btn_generate_cpf.clicked.connect(self.generator_cpf)
        self.btn_validate_cpf.clicked.connect(self.validator_cpf)
        self.copy_cpf.clicked.connect(self.get_copy_cpf)

    def get_copy_cpf(self):
        cpf = self.return_label.text()
        cpf = re.sub('[^0-9]', '', cpf)
        if cpf:
            cb = QGuiApplication.clipboard()
            if cb:
                cb.clear(mode=cb.Clipboard ) #type: ignore
                cb.setText(cpf, mode=cb.Clipboard) #type: ignore


    def generator_cpf(self):
        self.return_label.setText(generate_cpf())

    def validator_cpf(self):
        cpf = self.input_cpf.text()
        self.return_label.setText(str(validate_cpf(cpf)))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CpfCheckGenerator()
    window.show()
    app.exec_()

