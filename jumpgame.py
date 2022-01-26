cache = [[-1 for i in range(100)] for j in range(100)]
N = 0

def game2(board, y, x):
    if y == N - 1 and x == N - 1:
        return 1

    if y >= N or x >= N:
        return 0

    if cache[y][x] != -1:
        return cache[y][x]
    jump_size = board[y][x]
    cache[y][x] = (game2(board, y+jump_size, x) or game2(board, y, x+jump_size))
    return cache[y][x]

def game(board, y, x):
    board_size = len(board)
    if y == board_size-1 and x == board_size-1:
        return True

    if y >= board_size or x >= board_size:
        return False

    jump = board[y][x]
    return game(board, y+jump, x) or game(board, y, x+jump)


def test():
    test_case = int(input())
    for t in range(test_case):
        N = int(input())
        board = []
        for i in range(N):
            board.append(list(map(int, input())))
        game(board, 0, 0)