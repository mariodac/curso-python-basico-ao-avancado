from time import sleep
from threading import Thread

def take_time(text, time_,):
    sleep(time_)
    print(text)

t1 = Thread(target=take_time, args=('Olá mundo! 1', 5))

t1 = t1.start()


t2 = Thread(target=take_time, args=('Olá mundo! 2', 3))
t2 = t2.start()

t3 = Thread(target=take_time, args=('Olá mundo! 3', 1))
t3 = t3.start()

for i in range(15):
    print(i)
    sleep(.5)
