def dfs(G, S, C, u):
    if u in S: return
    S.add(u)
    for v in G[u]:
        dfs(G, S, C, v)
    C.append(u)

def ts(G):
    S, C = set(), []
    for u in G:
        dfs(G, S, C, u)
    C.reverse()
    return C

def tr(G):
    GT = {u:set() for u in G}
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    GT, S, CS = tr(G), set(), []
    for u in ts(G):
        if u in S: continue
        C = []
        dfs(GT, S, C, u)
        CS.append(C)
    return CS

g = {'a': {'b', 'c'}, 'b': {'d', 'e', 'i'}, 'c': {'d'}, 'd':{'a', 'h'}, 'e': {'f'}, 'f':{'g'}, 'g':{'e', 'h'}, 'h':{'i'}, 'i':{'h'}}
print(ts(g))
print(scc(g))
