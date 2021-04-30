def perms(a, k):
    for i in range(k, len(a)):
        a[k], a[i] = a[i], a[k]
        perms(a, k+1)
        a[k], a[i] = a[i], a[k]
    if k+1 == len(a):
        print(a)

perms([0, 1, 2], 0)
