from math import inf
from heapq import *

def dijk(G, s):
    Q, D, P = [(0, s)], {s: 0}, {}
    while Q:
        d, u = heappop(Q)
        if d > D[u]: continue
        D[u] = d
        for v in G[u]:
            d = D.get(u, inf) + G[u][v]
            if d < D.get(v, inf):
                D[v], P[v] = d, u
                heappush(Q, (d, v))
    return D, P

g = {'1': {'2': 7, '3': 9, '6': 14},
     '2': {'1': 7, '3': 10, '4': 15},
     '3': {'1': 9, '2': 10, '4': 11, '6': 2},
     '4': {'2': 15, '3': 11, '5': 6},
     '5': {'4': 6, '6': 9},
     '6': {'1': 14, '3': 2, '5': 9}}

from pprint import pprint
pprint(dijk(g, '1'))
neg = {'4':{}, '5':{'7':2}, '2':{'1':2, '3':-7, '0':6}, '1':{'3':3, '4':6}, '3':{'4':5}, '0':{'4':1}}
pprint(dijk(neg, '2'))
neg = {'0': {'1':1, '2':10}, '1':{'3':2}, '2':{'3':-10}, '3':{'4': 3}, '4':{}}
pprint(dijk(neg, '0'))
