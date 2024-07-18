from threading import Thread
from time import sleep
class MyThread(Thread):
    def __init__(self, text, time_):
        self.text = text
        self.time_ = time_

        super().__init__()

    def run(self):
        sleep(self.time_)
        print(self.text)


t1 = MyThread('Thread 1', 5)
t1.start()

while t1.is_alive():
    print('Esperando a thread.')
    sleep(1)	

t1.join()
print('Executando thread 2')

t2 = MyThread('Thread 2', 1)
t2.start()

t3 = MyThread('Thread 3', 3)
t3.start()

for i in range(15):
    print(i)
    sleep(1)