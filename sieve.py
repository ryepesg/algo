def sieve(n):
    a = [True]*n
    for i in range(3, int(n**.5)+1, 2):
        if a[i]:
            for j in range(i*i, n, i):
                a[j] = False
    return [2] + [p for p in range(3, n, 2) if a[p]]

print(sieve(50))
