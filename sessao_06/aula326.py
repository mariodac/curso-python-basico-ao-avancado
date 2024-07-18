from time import sleep
from threading import Thread
from threading import Lock

class Tickets():
    def __init__(self, stock) -> None:
        self.stock = stock
        # metódo para travar a execução de uma thread
        self.lock = Lock()

    def sell(self, amount):
        # trava a thread atual
        self.lock.acquire()
        if self.stock < amount:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return
        
        sleep(1)
        
        self.stock -= amount
        print(f"Você comprou {amount} ingresso(s). Ainda temos {self.stock}")

        # libera a execução da próxima thread
        self.lock.release()

if __name__ == '__main__':
    tickets = Tickets(100)
    tickets.sell(10)

    for i in range(1, 20):
        t = Thread(target=tickets.sell, args=(i,))
        t.start()

    print(tickets.stock)