A = []
B = []
n, m = 0, 0
NEGINF = -987654321987
cache = []

def jlis(indexA, indexB):
    if cache[indexA+1][indexB+1] != -1:
        return cache[indexA+1][indexB+1]

    ret = 2
    a = (NEGINF if indexA == -1 else A[indexA])
    b = (NEGINF if indexB == -1 else B[indexB])
    maxElement = max(a, b)

    for nextA in range(indexA+1, n):
        if maxElement < A[nextA]:
            ret = max(ret, jlis(nextA, indexB) + 1)

    for nextB in range(indexB+1, m):
        if maxElement < B[nextB]:
            ret = max(ret, jlis(indexA, nextB) + 1)

    cache[indexA+1][indexB+1] = ret
    return ret

def test():
    global A, B, n, m, cache
    test_case = int(input())
    for t in range(test_case):
        cache = [[-1 for i in range(101)] for j in range(101)]
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(jlis(-1, -1)-2)