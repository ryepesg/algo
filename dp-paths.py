from math import inf
from functools import lru_cache

@lru_cache()
def sp(v):
    if v==s: return 0
    m = inf
    for u in G:
        if v != u and v in G[u]:
            m = min(m, sp(u) + G[u][v])
    return m

from pprint import pprint
from string import ascii_lowercase
a, b, c, d, e, f, g, h = ascii_lowercase[:8]
G = {a: {b:2, c:1, d:3, e:9, f:4},
     b: {c:4, e:3},
     c: {d:8, f:1},
     d: {e:7},
     e: {f:5},
     f: {}}
s = a
pprint(G)
pprint({v:sp(v) for v in G})
print(sp.cache_info())
