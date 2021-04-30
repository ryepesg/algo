from math import inf
from functools import lru_cache

@lru_cache(1<<32)
def dp(val):
    global coins
    if val in coins: return 1
    if val == 0: return 0
    if val < 0: return inf
    return 1 + min(dp(val-c) for c in coins)

def change(cs, val):
    global coins
    coins = cs
    dp.cache_clear()
    print(dp(val))
    print({i:dp(i) for i in range(val+1)})
    print()

change({6, 5, 2}, 10)
change({6, 5, 1}, 9)
