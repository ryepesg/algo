def convexh(points):
    ps = sorted(set(points))
    if len(ps) < 2: return ps
    def ccw(o, a, b):
        cross = (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        return cross > 0
    L, U = [], []
    for p in ps:
        while len(L) > 1 and not ccw(L[-2], L[-1], p):
            L.pop()
        L.append(p)
    for p in reversed(ps):
        while len(U) > 1 and not ccw(U[-2], U[-1], p):
            U.pop()
        U.append(p)
    return L[:-1] + U[:-1]

assert convexh([(i//10, i%10) for i in range(100)]) == [(0, 0), (9, 0), (9, 9), (0, 9)]
assert convexh([(1, 1), (1, 1), (1, 1)]) == [(1, 1)]
