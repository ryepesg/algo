def find(P, i):
    if P[i] != i:
        P[i] = find(P, P[i])
    return P[i]

def union(P, R, i, j):
    u = find(P, i)
    v = find(P, j)
    if u==v: return False
    if R[u] > R[v]:
        P[v] = u
    else:
        P[u] = v
        if R[u] == R[v]:
            R[v] += 1
    return True

def krusk(G):
    T, P, R = set(), {u:u for u in G}, {u:0 for u in G}
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    for _, u, v in sorted(E):
        if union(P, R, u, v):
            T.add((u, v))
    return T

G = {'a':{'e':1, 'b':3}, 'b':{'a':3, 'c':5, 'e':4}, 'c':{'b':5, 'e':6, 'd':2}, 'd':{'c':2, 'e':7}, 'e':{'a':1, 'b':4, 'c':6, 'd':7}}
print(sorted(krusk(G)))
