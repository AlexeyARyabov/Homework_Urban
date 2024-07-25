import random

first = int(random.choice(range(3, 21)))
print(f'случайное число {first}')
my_pass = ''
for i in range(1, first):

    for j in range(i + 1, first):
        if first % (i + j) == 0:
            my_pass = my_pass + str(i) + str(j)

print('пароль', my_pass)
