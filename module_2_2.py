first = int(input("ведите первое число: "))
second = int(input("ведите второе число: "))
third = int(input("ведите третье число: "))

if first==second==third:
    print('одинаковых чисел:', 3)
elif first == second != third or first == third !=second or second==third!=first:
    print('одинаковых чисел:', 2)
else:
    print('одинаковых чисел:', 0)