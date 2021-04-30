def dfs(u, d):
    global k
    E[k], I[u] = (u, d), k
    k += 1
    for v in G[u]:
        dfs(v, d+1)
        E[k] = (u, d)
        k += 1

def build():
    global k, I
    k, I = 0, {}
    dfs('0', 0)

def lca(u, v):
    if I[u] > I[v]:
        u, v = v, u
    idx = query(I[u], I[v])
    return E[idx][0]

def buildST(v=1, tl=0, tr=None):
    if tr is None: tr = n-1
    if tl==tr: T[v] = tl
    else:
        vl, vr, tm = 2*v, 2*v+1, (tl+tr)//2
        buildST(vl, tl, tm)
        buildST(vr, tm+1, tr)
        p1, p2 = T[vl], T[vr]
        T[v] = p1 if a[p1] <= a[p2] else p2

from math import inf
def query(i, j, v=1, tl=0, tr=None):
    if tr is None: tr = n-1
    if i > j: return inf
    if i<=tl and tr<=j: return T[v]
    vl, vr, tm = 2*v, 2*v+1, (tl+tr)//2
    p1 = query(i, min(tm, j), vl, tl, tm)
    p2 = query(max(i, tm+1), j, vr, tm+1, tr)
    if p1 == inf: return p2
    if p2 == inf: return p1
    return p1 if a[p1] <= a[p2] else p2

G = {'0': {'1', '7'},
     '1': {'2', '3', '6'},
     '2': {},
     '3': {'4', '5'},
     '4': {},
     '5': {},
     '6': {},
     '7': {'8', '9'},
     '8': {},
     '9': {}}

k, K = 0, len(G)
E, I = [(0, 0)]*(2*K-1), {}
build()

a = [d for u, d in E]
n = len(a)
T = [0]*(4*n)
buildST()

#print("I", I)
#print("E", [u for u, d in E])
#print("L", a)

assert lca('4', '6') == '1'
assert lca('6', '9') == '0'  
assert lca('4', '5') == '3'
assert lca('8', '0') == '0'
assert lca('8', '9') == '7'
assert lca('8', '5') == '0'

print(lca('4', '5'))
