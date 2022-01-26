cache = [-1 for i in range(101)]
S = []
n = 0

def lis(S):
    if len(S) == 0:
        return 0
    ret = 0
    for i in range(len(S)):
        B = []
        for j in range(i+1, len(S)):
            if S[i] < S[j]:
                B.append(S[j])
        ret = max(ret, 1 + lis(B))

    return ret

def lis2(start):
    if cache[start] != -1:
        return cache[start]

    ret = 1
    for next in range(start+1, n):
        if S[start] < S[next]:
            ret = max(ret, lis2(next) + 1)
    cache[start] = ret
    return ret

#S[-1] = inf result : lis3(-1)-1
def lis3(start):
    if cache[start+1] != -1:
        return cache[start+1]
    ret = 1
    for next in range(start+1, n):
        if start == -1 or S[start] < S[next]:
            ret = max(ret, lis3(next)+1)
    cache[start+1] = ret
    return ret


def test():
    global n
    global S
    test_case = int(input())
    for t in range(test_case):
        S = list(map(int, input().split()))
        n = len(S)
        lis(S)