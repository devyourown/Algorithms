boggle = [['U', 'R', 'L', 'P', 'M'],
          ['X', 'P', 'R', 'E', 'T'],
          ['G', 'I', 'A', 'E', 'T'],
          ['X', 'T', 'N', 'Z', 'Y'],
          ['X', 'O', 'Q', 'R', 'S']]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def hasWord(y, x, word):
    if(y > 4 or y < 0 or x < 0 or x > 4):
        return False
    if(boggle[y][x] != word[0:1]):
        return False
    if(len(word) == 1):
        return True
    for direction in range(0, 8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        if(hasWord(nextY, nextX, word[1:])):
            return True
    return False


