from random import randint

def merge(a, b):
    if not a or not b: return a if a else b
    if b.y > a.y:
        b.l, v = merge(a, b.l), b
    else:
        a.r, v = merge(a.r, b), a
    v.recalc()
    return v

def split(v, k):
    if not v: return None, None
    if k <= v.x:
        a, v.l = split(v.l, k)
        v.recalc()
        return a, v
    else:
        v.r, b = split(v.r, k)
        v.recalc()
        return v, b

def traverse(v):
    if not v: return []
    return traverse(v.l) + [v.x] + traverse(v.r)

class Treap:
    class Node:
        def __init__(self, k):
            self.x = k
            self.y = randint(0, 1<<48)
            self.l = self.r = None
            self.sz = 1

        def recalc(self):
            self.sz = 1 + (self.l.sz if self.l else 0) + (self.r.sz if self.r else 0)

        def __repr__(self):
            return str(self.x)

    def __init__(self):
        self.root = None

    def insert(self, k):
        a, b = split(self.root, k)
        v = self.Node(k)
        self.root = merge(merge(a, v), b)
        return v

    def remove(self, k):
        a, m = split(self.root, k)
        _, b = split(m, k+1)
        self.root = merge(a, b)

    def kth(self, k):
        p = self.root
        while p:
            lsz = p.l.sz if p.l else 0
            if k < lsz:
                p = p.l
            elif k > lsz:
                p = p.r
                k -= lsz + 1
            else: return p

    def succ(self, v):
        if v.r:
            p = v.r
            while p.l:
                p = p.l
            return p
        s = None
        p = self.root
        while p:
            if v.x < p.x:
                s = p
                p = p.l
            elif v.x > p.x:
                p = p.r
            else: return s

    def pred(self, v):
        if v.l:
            p = v.l
            while p.r:
                p = p.r
            return p
        s = None
        p = self.root
        while p:
            if v.x < p.x:
                p = p.l
            elif v.x > p.x:
                s = p
                p = p.r
            else: return s


t = Treap()
t.insert(5)
t.insert(3)
v = t.insert(7)
t.insert(1)
t.remove(1)
w = t.insert(8)
t.insert(6)
t.insert(2)
t.remove(6)
vv = t.insert(1)
ww = t.insert(0)

print(traverse(t.root))
print(t.pred(v), v.x, t.succ(v))
print(t.pred(vv), vv.x, t.succ(vv))
print(t.pred(w), w.x, t.succ(w))
print(t.pred(ww), ww.x, t.succ(ww))

print([t.kth(i) for i in range(t.root.sz)])
