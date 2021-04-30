from math import inf

def floydw(G):
    P = {}
    for u in G:
        for v in G:
            if v not in G[u]:
                G[u][v] = inf
                P[u, v] = None
            else:
                P[u, v] = u
    for k in G:
        for u in G:
            for v in G:
                d = G[u][k] + G[k][v]
                if d < G[u][v]:
                    G[u][v] = d
                    P[u, v] = P[k, v]
    return P

G = {0: {1:6, 2:8},
     1: {4:11},
     2: {3:9},
     3: {},
     4: {5:3},
     5: {2:7, 3:4}}

from pprint import pprint
pred = floydw(G)
pprint(G)
pprint(pred)
