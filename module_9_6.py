from itertools import  combinations


def all_variants(text):
    i = 1
    while i <= len(text):
        for comb in combinations(text, i):
            yield ''.join(comb)
        i += 1

a = all_variants('abc')
for x in a:
    print(x)
