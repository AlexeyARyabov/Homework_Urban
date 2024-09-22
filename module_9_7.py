def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        k = 0
        for i in range(2, res // 2 + 1):
            if not res % i:
                k = k + 1
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    summa = a + b + c
    return summa

result = sum_three(2, 3, 6)
print(result)