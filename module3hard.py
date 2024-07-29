summer = 0


def calculate_structure_sum(data_str):
    global summer
    for elem in data_str:
        if isinstance(elem, int):
            summer += elem
        if isinstance(elem, str):
            summer += len(elem)
        if isinstance(elem, list):
            for el1 in elem:
                if isinstance(el1, int):
                    summer += el1
                elif isinstance(el1, str):
                    summer += len(el1)
                else:
                    calculate_structure_sum(el1)
        if isinstance(elem, dict):
            for key_ in elem.keys():
                summer += len(key_)
            for value_ in elem.values():
                summer += value_
        if isinstance(elem, tuple):
            for el_tuple in elem:
                if isinstance(el_tuple, int):
                    summer += el_tuple
                elif isinstance(el_tuple, str):
                    summer += len(el_tuple)
                else:
                    calculate_structure_sum(el_tuple)
    return summer


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum(data_structure)
print(summer)
