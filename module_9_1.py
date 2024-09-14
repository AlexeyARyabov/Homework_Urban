def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        func_value = func(int_list)
        results.update({func.__name__: func_value})
    return results

def min_el(int_list):
    return min(int_list)

def max_el(int_list):
    return min(int_list)

def len_list(int_list):
    return len(int_list)

def sum_el(int_list):
    return sum(int_list)

def sorted_el(int_list):
    return sorted(int_list)
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
