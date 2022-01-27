INF = 987654321
n, s = 0, 0
p_sum = []
p_sq_sum = []
A = []

cache = []

def precalc():
    sorted(A)
    p_sum[0] = A[0]
    p_sq_sum[0] = A[0] * A[0]
    for i in range(1, n):
        p_sum[i] = p_sum[i-1] + A[i]
        p_sq_sum[i] = p_sq_sum[i-1] + A[i] * A[i]


def min_error(lo, hi):
    sum = p_sum[hi] - (0 if lo == 0 else p_sum[lo-1])
    sq_sum = p_sq_sum[hi] - (0 if lo == 0 else p_sq_sum[lo-1])
    m = int(round(sum/(hi-lo+1)))
    ret = sq_sum - 2 * m * sum + m * m * (hi-lo+1)
    return ret


def quantize(fromN, parts):
    if fromN == n:
        return 0

    if parts == 0:
        return INF

    if cache[fromN][parts] != -1:
        return cache[fromN][parts]

    ret = INF
    for part_size in range(1, n-fromN+1):
        ret = min(ret, min_error(fromN, fromN + part_size - 1) +
                  quantize(fromN+part_size, parts-1))
    return ret

def test():
    global n, s, seq, cache, A
    test_case = int(input())
    for _ in range(test_case):
        cache = [[-1 for _ in range(11)] for _ in range(101)]
        n, s = map(int, input().split())
        A = list(map(int, input().split()))
        quantize(0, 0)
