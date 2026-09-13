if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    res = None
    minSteps = float('inf')
    
    for target in arr:
        curSteps = sum(abs(x - target) for x in arr)
        if curSteps < minSteps:
            minSteps = curSteps
            res = target
    
    print(minSteps, res, sep = " ")