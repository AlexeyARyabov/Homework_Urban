from threading import Thread
from time import sleep
from random import randint
import queue

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
    q = queue.Queue()
    def __init__(self, *tables):
        self.tables = []
        for table in tables:
            self.tables.append(table)

    def guest_arrival(self, *guests):
        global q
        for guest in guests:
            if Table.guest is None:
                Table.guest = guest
                guest = Guest(Table.guest)
                guest.start()
                guest.join()
                print(f'{guest} сел(-а) за стол номер {Table.number}')
            else:
                q.put(guest)
                print(f'{guest} в очереди')

    def discuss_guests(self):
        while not q.empty() or not Table.guest is None:
            if Table.guest and Guest.is_alive():
                print(f'{Table.guest} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {Table.number} свободен')
                Table.guest = None
            if Table.guest is None:
                Table.guest = q.get()
                print(f'{Table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {Table.number}')
                Table.guest.start()


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
