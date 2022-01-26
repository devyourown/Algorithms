def solve(fence, left, right):
    if(left == right):
        return fence[left]
    mid = (left+right)/2
    ret = max(solve(fence, left, mid), solve(fence, mid+1, right))
    lo = mid, hi = mid+1
    height = min(fence[lo], fence[hi])
    ret = max(ret, height*2)
    while(left < lo or hi < right):
        if(hi<right and (lo == left or fence[lo-1] < fence[hi+1])):
            hi += 1
            height = min(height, fence[hi])
        else :
            lo -= 1
            height = min(height, fence[lo])
        ret = max(ret, height*(hi-lo+1))
    return ret

def makeRecWood(fence):
    ret = 0
    N = len(fence)
    for left in range(N):
        minHeight = fence[left]
        for right in range(N):
            minHeight = min(minHeight, fence[right])
            ret = max(ret, (right-left+1)*minHeight)
    return ret


def test():
    test_case = int(input())
    for i in range(test_case):
        N = int(input())
        fences = list(map(int, input().split()))
        result = makeRecWood(fences)
        print(result)