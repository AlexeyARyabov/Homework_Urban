import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        while file.readline():
            all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
'''start = datetime.datetime.now()

for filename in filenames:
        read_info(filename)

end = datetime.datetime.now()
print(end - start)'''

# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)