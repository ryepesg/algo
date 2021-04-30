def zf(s, m):
    n = len(s)
    z = [0]*n
    L = R = 0
    idx = []
    for i in range(1, n):
        if i <= R:
            z[i] = min(z[i-L], R-i+1)
        while i+z[i] < n and s[i+z[i]] == s[z[i]]:
            z[i] += 1
        if i+z[i]-1 > R:
            L, R = i, i+z[i]-1
        if z[i] == m:
            idx.append(i-m-1)
    return z, idx

def pf(z):
    n = len(z)
    p = [0]*n
    for i in range(1, n):
        if z[i]:
            for j in range(z[i]-1, -1, -1):
                if p[i+j]: break
                p[i+j] = j+1
    return p

z, idx = zf("aba$ababaca", 3)
print(z, idx)

print()
z, idx = zf("abcabcd", 7)
print(pf(z))

print()
z, idx = zf("aabaaab", 7)
print(pf(z))
