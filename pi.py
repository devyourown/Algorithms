N = []
INF = 987654321
cache = [-1 for _ in range(10002)]

def classify(a, b):
    M = N[a:b]
    if M == [M[0] for _ in range(len(M))]:
        return 1
    progressive = True

    for i in range(len(M)-1):
        if M[i+1] - M[i] != M[1] - M[0]:
            progressive = False

    if progressive and abs(M[1] - M[0]) == 1:
        return 2

    alternating = True
    for i in range(len(M)):
        if(M[i] != M[i%2]):
            alternating = False

    if(alternating): return 4
    if(progressive): return 5
    return 10

def memorize(begin):
    if begin == len(N):
        return 0

    if cache[begin] != -1:
        return cache[begin]

    ret = INF

    for L in range(3, 6):
        if begin+L <= len(N):
            ret = min(ret, memorize(begin + L) + classify(begin, begin + L))

    cache[begin] = ret
    return ret



def test():
    test_case = int(input())
    for t in range(test_case):
        s = input()
        for piece in s:
            N.append(int(piece))
        print(memorize(0))
