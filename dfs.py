def dfs(G, S, stack, u):
    if u in S: return
    global cyc
    S.add(u)
    stack.add(u)
    print(u)
    for v in G[u]:
        if cyc: return
        if v in stack:
            cyc = True
        dfs(G, S, stack, v)
    stack.discard(u)

cyc = False
G = {0: {1, 3}, 1:{}, 2:{0, 1}, 3:{2}}
S = set()
for u in G:
    dfs(G, S, set(), u) 
if cyc: print("ciclo!")

print()
cyc = False
G = {0: {1, 3}, 1:{}, 2:{0, 1}, 3:{1}}
S = set()
for u in G:
    dfs(G, S, set(), u)
if cyc: print("ciclo!")

