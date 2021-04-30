from math import inf

a = [1, 4, -2, 1, 7, 2]
n = len(a)
T = [0]*(4*n)

def build(v=1, tl=0, tr=n-1):
    if tl==tr: T[v] = a[tl]
    else:
        vl, vr, tm = 2*v, 2*v+1, (tl+tr)//2
        build(vl, tl, tm)
        build(vr, tm+1, tr)
        T[v] = min(T[vl], T[vr])

def update(i, val, v=1, tl=0, tr=n-1):
    if tl==tr: T[v] = val
    else:
        vl, vr, tm = 2*v, 2*v+1, (tl+tr)//2
        if i <= tm: update(i, val, vl, tl, tm)
        else: update(i, val, vr, tm+1, tr)
        T[v] = min(T[vl], T[vr])

def query(i, j, v=1, tl=0, tr=n-1):
    if i > j: return inf
    if i <= tl and tr <= j: return T[v]
    vl, vr, tm = 2*v, 2*v+1, (tl+tr)//2
    return min(query(i, min(tm, j), vl, tl, tm),
               query(max(i, tm+1), j, vr, tm+1, tr))

for i, e in enumerate(a):
    update(i, e)
    print(query(i, i), end=" ")
print()
build()
for i, e in enumerate(a):
    print(query(i, i), end=" ")
print()
print(query(0, n-1))
