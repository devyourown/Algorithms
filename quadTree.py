tree_num = -1

def reverse(tree):
    global tree_num
    tree_num = tree_num + 1
    if(tree[tree_num] == "w" or tree[tree_num] == "b"):
        return tree[tree_num]
    upperLeft = reverse(tree)
    upperRight = reverse(tree)
    lowerLeft = reverse(tree)
    lowerRight = reverse(tree)
    return "x"+lowerLeft+lowerRight+upperLeft+upperRight

def test():
    test_case = int(input())
    for t in range(test_case):
        originalTree = input()
        print(reverse(originalTree))
