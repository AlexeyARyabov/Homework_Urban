from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting_time = randint(3, 10)
        sleep(waiting_time)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    guest = Guest(table.guest)
                    guest.start()
                    guest.join()
                    print(f'{table.guest} сел(-а) за стол номер {table.number}')
                    break
                elif all(not table.guest is None for table in self.tables):
                    self.queue.put(guest.name)
                    print(f'{guest.name} в очереди')
                    break


    def discuss_guests(self):
        while not self.queue.empty() or any(not table.guest is None for table in self.tables):
            for guest in guests:
                for table in self.tables:
                    if not table.guest is None and not guest.is_alive():
                        print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        break
                    elif table.guest is None and not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        guest = Guest(table.guest)
                        guest.start()
                        guest.join()



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

