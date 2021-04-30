from functools import lru_cache

@lru_cache(1<<32)
def d(i, j):
    global a, b
    if i < 0: return j + 1
    if j < 0: return i + 1
    neq = a[i] != b[j]
    return min(d(i-1, j) + 1,
               d(i, j-1) + 1,
               d(i-1, j-1) + neq)

def align(i, j):
    global a, b
    if i < 0 and j < 0: return
    if d(i, j) == d(i-1, j) + 1:
        align(i-1, j)
        print(a[i], '-')
    elif d(i, j) == d(i, j-1) + 1:
        align(i, j-1)
        print('-', b[j])
    else:
        align(i-1, j-1)
        print(a[i], b[j])

def edist(s1, s2):
    global a, b
    a, b = s1, s2
    d.cache_clear()
    print(d(len(a)-1, len(b)-1))
    align(len(a)-1, len(b)-1)
    print()

edist("editing", "distance")
edist("kitten", "sitting")
edist("geek", "gesek")
edist("hola", "hol")
