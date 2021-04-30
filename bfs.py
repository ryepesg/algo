from collections import deque

def bfs(G, s):
    Q, D, P = deque([s]), {s:0}, {}
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in D:
                D[v], P[v] = D[u]+1, u
                Q.append(v)
    return D, P

G = {'s':['a', 'x'],
     'a':['s', 'z'],
     'z':['a'],
     'x':['s', 'd', 'c'],
     'd':['x', 'c', 'f'],
     'c':['x', 'd', 'f', 'v'],
     'v':['c', 'f'],
     'f':['d', 'c', 'v']}

d, parent = bfs(G, 's')
print(d)
print(parent)
