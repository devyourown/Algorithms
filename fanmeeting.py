def meeting(group, fans):
    full_hug = len(fans)-len(group)+1
    ret = 0
    for i in range(full_hug):
        ok = True
        for j in range(len(group)):
            if fans[i+j] == "M" and group[j] == "M":
                ok = False
                break
        if ok:
            ret += 1
    return ret


def test():
    test_case = int(input())
    for t in range(test_case):
        group = input()
        fans = input()
        print(meeting(group, fans))
