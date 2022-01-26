W = ""
S = ""
cache = [[-1 for i in range(101)] for j in range(101)]

def matchMemoized(w, s):
    if cache[w][s] != -1:
        return cache[w][s]
    w_size = len(W)
    s_size = len(S)

    while(s < s_size and w < w_size and (W[w] == "?" or W[w] == S[s])):
        w += 1
        s += 1

    if(w == w_size):
        cache[w][s] = (s == s_size)
        return cache[w][s]
    if(W[w] == "*"):
        for skip in range(s_size):
            if(matchMemoized(w+1, s+skip)):
                cache[w][s] = 1
                return cache[w][s]
    cache[w][s] = 0
    return cache[w][s]

def match(pattern, file):
    pos = 0
    pattern_size = len(pattern)
    file_size = len(file)
    while(pos < pattern_size and pos < file_size and
          (pattern[pos] == "?" or pattern[pos] == file[pos])):
        pos += 1

    if(pos == pattern_size):
        return pos == file_size
    if(pattern[pos] == "*"):
        for skip in range(file_size):
            if match(pattern[pos+1:], file[pos+skip:]):
                return True
    return False

def howManyWild(pattern, files):
    global W, S
    result = []
    W = pattern
    for file in files:
        S = file
        if matchMemoized(0, 0):
            result.append(file)


    return result

def test():
    test_case = int(input())
    for t in range(test_case):
        pattern = input()
        file_num = int(input())
        list = []
        for i in range(file_num):
            list.append(input())
        ret_list = howManyWild(pattern, list)
        for ret in ret_list:
            print(ret)