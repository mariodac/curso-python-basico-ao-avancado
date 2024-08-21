import sys
import time
from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QWidget
from workerui import Ui_myWidget


# cria um worker e uma thread para executar o trabalho
# metodo que consegue obter o inicio, progresso e fim do worker
class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = "0"
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.hardWork1)
        self.pushButton_2.clicked.connect(self.hardWork2)

    # gerencia os workers e as threads
    def hardWork2(self):

        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        # apagar da memoria apos terminar o trabalho
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self, value):
        self.pushButton_2.setDisabled(True)
        self.label_2.setText(value)
        print("worker iniciado")

    def worker2Progressed(self, value):
        self.label_2.setText(value)
        print("em progresso")

    def worker2Finished(self, value):
        self.label_2.setText(value)
        self.pushButton_2.setDisabled(False)
        print("worker finalizado")

    def hardWork1(self):

        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        # apagar da memoria apos terminar o trabalho
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        thread.start()

    def worker1Started(self, value):
        self.pushButton.setDisabled(True)
        self.label.setText(value)
        print("worker iniciado")

    def worker1Progressed(self, value):
        self.label.setText(value)
        print("em progresso")

    def worker1Finished(self, value):
        self.label.setText(value)
        self.pushButton.setDisabled(False)
        print("worker finalizado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
