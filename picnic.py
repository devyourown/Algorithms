couples = [[False for x in range(10)] for y in range(10)]
numOfStudents = 0
result = []

def makeCouples(taken):
    firstFree = -1
    for i in range(numOfStudents):
        if(not taken[i]):
            firstFree = i
            break
    if(firstFree == -1):
        return 1

    ret = 0

    for pairWith in range(firstFree+1, numOfStudents):
        if(not taken[pairWith] and couples[firstFree][pairWith]):
                taken[firstFree] = taken[pairWith] = True
                ret += makeCouples(taken)
                taken[firstFree] = taken[pairWith] = False
    return ret

def test():
    test_case = int(input())
    for case in range(test_case):
        numOfStudents, numOfCouples = map(int, input().split())
        strOfInput = list(input().split())
        for j in range(0, len(strOfInput), 2):
            x = int(strOfInput[j])
            y = int(strOfInput[j + 1])
            couples[x][y] = True
            couples[y][x] = True
        taken = [False for i in range(10)]
        result.append(makeCouples(taken))