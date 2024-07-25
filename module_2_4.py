numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0
for i in range(len(numbers)):

    if numbers[i] > 1:
            for j in range(i+1):
                if numbers[i] % numbers[j] == 0:
                    k+=1
    if k == 2:
        primes.append(numbers[i])
    elif k > 2:
        not_primes.append(numbers[i])
    k = 0
print(primes)
print(not_primes)