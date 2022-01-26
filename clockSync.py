switch = [[0, 1, 2], [3, 7, 9, 11], [4, 10, 14, 15], [0, 4, 5, 6, 7],
          [6, 7, 8, 10, 12], [0, 2, 14, 15], [3, 14, 15], [4, 5, 7, 14, 15],
          [1, 2, 3, 4, 5], [3, 4, 5, 9, 13]]
INF = 123456789

def isSynced(clocks):
    ok = True
    for i in range(16):
        if(clocks[i] != 12):
            ok = False
            break
    return ok

def sync(clocks, switchNum, pushed):
    if(switchNum == 10):
        return INF
    if(isSynced(clocks)):
        return pushed

    result = INF
    for i in range(4):
        ret = sync(clocks, switchNum + 1, pushed + i)
        result = min(ret, result)
        for num in switch[switchNum]:
            clocks[num] += 3
            if(clocks[num] == 15):
                clocks[num] = 3
    return result

def test():
    test_case = int(input())
    for t in range(test_case):
        clocks = list(map(int, input().split()))
        print(sync(clocks, 0, 0))