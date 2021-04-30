from math import inf
from collections import deque

def bellf(G, s):
    Q, S, D, P = deque([s]), {s}, {s:0}, {}
    k, K = 0, 2*len(G)
    while Q:
        u = Q.popleft()
        S.discard(u)
        for v in G[u]:
            d = D[u] + G[u][v]
            if d < D.get(v, inf):
                D[v], P[v] = d, u
                if v not in S:
                    S.add(v)
                    Q.append(v)
        k += 1
        if k == K:
            return True, D, P
    return False, D, P

from pprint import pprint
from string import ascii_lowercase

a, b, c, d, e, f, g, h = ascii_lowercase[:8]
G = {a: {b:2, c:1, d:3, e:9, f:4},
     b: {c:4, e:3},
     c: {d:8},
     d: {e:7},
     e: {f:5},
     f: {c:2, g:2, h:2},
     g: {f:1, h:6},
     h: {f:9, g:8}}
pprint(bellf(G, a))

a, b, c = ascii_lowercase[:3]
G = {a: {b:2, c:1},
     b: {c:-4},
     c: {a:1}}
pprint(bellf(G, a))
