import threading
from time import sleep
from random import randint

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for count in range(1, 101):
            while self.balance < 500:
                many = randint(5,500)
                self.balance += many
                print(f'Пополнение: {many}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for count in range(1, 101):
            many = randint(5,500)
            print(f'Запрос на {many}')
            if many <= self.balance:
                self.balance -= many
                print(f'Снятие: {many}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
