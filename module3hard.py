summer = 0


def calculate_structure_sum(*data_str):
    global summer
    for dat in data_str:
        if isinstance(dat, tuple) or isinstance(dat, list) or isinstance(dat, set):
            for elem in dat:
                calculate_structure_sum(elem)
        if isinstance(dat, dict):
            for key_ in dat.keys():
                summer += len(key_)
            for value_ in dat.values():
                summer += value_
        if isinstance(dat, int):
            summer += dat
        if isinstance(dat, str):
            summer += len(dat)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum(data_structure)

print(summer)
