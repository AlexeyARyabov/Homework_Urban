calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(my_str):
    len1 = len(my_str)
    str_up = my_str.upper()
    str_low = my_str.upper().lower()
    my_tuple = len1, str_up, str_low
    print(my_tuple)
    count_calls()


def is_contains(string, list_to_search):
    k = 0
    for i in list_to_search:
        if i.lower() == string:
            k += 1
    if k != 0:
        print(True)
    else:
        print(False)
    count_calls()




string_info(input('ведите слово: '))
is_contains(input('введите искомое слово: ').lower(), input('ввведите список для поиска: ').split())
string_info(input('ведите слово: '))
is_contains(input('введите искомое слово: ').lower(), input('ввведите список для поиска: ').split())

print(calls)
