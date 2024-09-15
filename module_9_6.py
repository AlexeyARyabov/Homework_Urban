from itertools import product, repeat


def all_variants(text):
    i = 1
    while i <= len(text):
        x = product(text, repeat=i)
        yield x
        i += 1

a = all_variants("abc")
for i in a:
    print(i)
