from collections import deque

def dfs(G, D, F, u, t, f):
    if u==t: return f
    for v in G[u]:
        if D.get(v, None) == D[u]+1 and G[u][v] > F[u][v]:
            df = dfs(G, D, F, v, t, min(f, G[u][v]-F[u][v]))
            if df > 0:
                F[u][v] += df
                F[v][u] -= df
                return df
    else: return 0

def dinic(G, s, t):
    flow = 0
    F = {u:{v:0 for v in G} for u in G}
    while True:
        Q, D = deque([s]), {s:0}
        while Q:
            u = Q.popleft()
            for v in G[u]:
                if v not in D and G[u][v] > F[u][v]:
                    D[v] = D[u] + 1
                    Q.append(v)
        if t not in D:
            return F, flow
        f = sum(G[s][v] for v in G[s]) - flow
        flow += dfs(G, D, F, s, t, f)


def show(F):
    print(", ".join(f"{i}->{k}:{v}" for i, row in F.items() for k, v in row.items() if v>0))

G = {0: {1:10, 2:10},
     1: {2:2, 3:4, 4:8},
     2: {4:9},
     3: {5:10},
     4: {3:6, 5:10},
     5: {}}

from pprint import pprint
F, flow = dinic(G, 0, 5)
print(f"{flow:<3}", end="| ")
show(F)

G = {'a':{'b':3, 'd':3},
     'b':{'c':4},
     'c':{'a':3, 'd':1, 'e':2},
     'd':{'e':2, 'f':6},
     'e':{'b':1, 'g':1},
     'f':{'g':9},
     'g':{}}
F, flow = dinic(G, 'a', 'g')
print(f"{flow:<3}", end="| ")
show(F)

a, b, c, d, e, f, g, h = range(8)
G = {a: {b:2, c:1, d:3, e:9, f:4},
     b: {c:4, e:3},
     c: {d:8},
     d: {e:7},
     e: {f:5},
     f: {c:2, g:2, h:2},
     g: {f:1, h:6},
     h: {f:9, g:8}}
F, flow = dinic(G, 0, 5)
print(f"{flow:<3}", end="| ")
show(F)

G = {a: {b:2, c:1},
     b: {c:-4},
     c: {a:1}}
F, flow = dinic(G, 0, 2)
print(f"{flow:<3}", end="| ")
show(F)
