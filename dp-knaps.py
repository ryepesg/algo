from functools import lru_cache

@lru_cache(1<<32)
def k(i, w):
    if i < 0 or w <= 0: return 0
    m = k(i-1, w)
    if W[i] > w: return m
    return max(m, k(i-1, w-W[i]) + V[i])

def choice(i, w, S=set()):
    if i < 0: return
    if k(i, w) == k(i-1, w):
        choice(i-1, w)
    else:
        S.add((W[i], V[i]))
        choice(i-1, w-W[i])
    return S

W = [6, 3, 4, 2]
V = [30, 14, 16, 9]
n = len(W)-1
print(k(n, 10))
print(choice(n, 10))
for i in range(-1, n+1):
    for w in range(10+1):
        print(f"{k(i, w):^2}", end=" ")
    print()
