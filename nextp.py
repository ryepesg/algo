def nextp(a):
    indices = range(len(a)-1, -1, -1)
    while True:
        print(a)
        for k in indices[1:]:
            if a[k] < a[k+1]: break
        else: return
        for i in indices:
            if a[k] < a[i]: break
        a[k], a[i] = a[i], a[k]
        a[k+1:] = a[k+1:][::-1]

nextp(list("dabc"))
