n = 0
tiles = []
MOD = 1000000007
cache = []

def tiling(N):
    if N <=  1:
        return 1
    if cache[N] != -1:
        return cache[N]

    cache[N] = (tiling(N-1) + tiling(N-2)) % MOD
    return (tiling(N-1) + tiling(N-2)) % MOD

def test():
    global n, tiles, cache
    test_case = int(input())
    for _ in range(test_case):
        cache = [-1 for _ in range(101)]
        n = int(input())
        tiles = [[0 for _ in range(n)] for _ in range(2)]