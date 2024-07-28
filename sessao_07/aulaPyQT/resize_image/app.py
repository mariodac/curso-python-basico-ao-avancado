import sys
import os
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

PATH_USER = os.getenv('USERPROFILE')

class ResizeImage(QMainWindow, Ui_MainWindow): #type:ignore
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.new_image = None

        self.btn_choose_file.clicked.connect(self.open_image)
        self.btn_resize.clicked.connect(self.resize_image)
        self.btn_save_image.clicked.connect(self.save_image)


    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Abrir Imagem', PATH_USER, "Image Files (*.png *.jpg *.bmp)")
        self.input_file.setText(image)
        self.original_image = QPixmap(image)
        self.label_img.setPixmap(self.original_image)
        self.input_width.setText(str(self.original_image.width()))
        self.input_height.setText(str(self.original_image.height()))

    def resize_image(self):
        width = int(self.input_width.text())
        self.new_image = self.original_image.scaledToWidth(width)
        self.label_img.setPixmap(self.new_image)
        self.input_width.setText(str(self.new_image.width()))
        self.input_height.setText(str(self.new_image.height()))

    def save_image(self):
        if self.new_image is not None:
            image, _ = QFileDialog.getSaveFileName(self.centralwidget, 'Salvar Imagem', PATH_USER, 'Image Files (*.png)')
            self.new_image.save(image, 'PNG')
        else:
            self.label_img.setStyleSheet('color: red; font-weight: 700;')
            self.label_img.setText('DEVE SELECIONAR UMA IMAGEM PARA SALVAR')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = ResizeImage()
    app.showMaximized()
    qt.exec_()