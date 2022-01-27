cache = []
N = 0
triangle = []

def max_path(y, x):
    if y == N-1:
        return triangle[y][x]
    if cache[y][x] != -1:
        return cache[y][x]

    ret = triangle[y][x]

    ret += max(max_path(triangle, y+1, x), max_path(triangle, y+1, x+1))
    cache[y][x] = ret
    return ret


def test():
    global cache, triangle
    test_case = int(input())
    for t in range(test_case):
        N = int(input())
        cache = [[-1 for i in range(N)] for j in range(N)]
        for n in range(N):
            triangle.append(list(map(int, input().split())))
