def bitmask_find(*xs, num=7):
    n = len(xs)
    for mask in range(1 << n):
        s = 0
        r = []
        for i in range(n):
            if mask & (1 << i):
                s += xs[i]
                r.append(xs[i])
            if s == num:
                print(xs[::-1])
                print(f"{mask:08b}")
                print(r[::-1], end="\n\n")
                return True
    return False




assert bitmask_find(3, 4)
assert bitmask_find(1, 2, 4)
assert bitmask_find(7)
assert bitmask_find(0, 7)
assert bitmask_find(1, 2, 3, 4, 5, 6, 7)
assert bitmask_find(2, 4, 5, 6)
assert bitmask_find(1, 2, 5)
assert not(bitmask_find(6, 4))
assert not(bitmask_find(1))
assert not(bitmask_find(1, 2))
assert not(bitmask_find(4, 5, 6))
