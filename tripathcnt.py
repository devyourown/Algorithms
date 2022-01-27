import trianglepath

count_cache = []
path_N = 0

def count(y, x):
    if y-1 == path_N:
        return 1

    if count_cache[y][x] != -1:
        return count_cache[y][x]

    ret = 0
    if(trianglepath.max_path(y+1, x+1) >= trianglepath.max_path(y+1, x)):
        ret += count(y+1, x+1)
    if(trianglepath.max_path(y+1, x+1) <= trianglepath.max_path(y+1, x)):
        ret += count(y+1, x)
    count_cache[y][x] = ret
    return ret