board = [[]]

shape = [
    [[0,0], [1,0], [0,1]],
    [[0,0], [0,1], [1,1]],
    [[0,0], [1,0], [1,1]],
    [[0,0], [1,0], [1,-1]]
]

def set(board, y, x, type, delta):
    ok = True
    for i in range(3):
        ny = y + shape[type][i][0]
        nx = x + shape[type][i][1]
        if(ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0])):
            ok = False
        else:
            board[ny][nx] += delta
            if((board[ny][nx]) > 1) :
                ok = False
    return ok

def cover(board):
    y = -1
    x = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                y = i
                x = i
                break
        if(y != -1):
            break
    if(y == -1):
        return 1
    ret = 0
    for type in range(4):
        if(set(board, y, x, type, 1)):
            ret += cover(board)
        set(board, y, x, type, -1)

    return ret

def test():
    test_case = int(input())
    for t in range(test_case):
        h, w = map(int, input().split())
        board = [[0 for i in range(w)] for j in range(h)]
        for i in range(h):
            j = 0
            for element in list(input().split()):
                if (element == '#'):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
                j+= 1
        print(cover(board))

