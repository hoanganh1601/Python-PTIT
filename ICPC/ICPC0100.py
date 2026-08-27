import math

if __name__ == '__main__':
    test = int(input())
    
    for _ in range(test):
        n = int(input())
        arr = list(map(int, input().split()))
        
        cnt = 0
        for i in range(1, n):
            minVal = min(arr[i], arr[i - 1])
            maxVal = max(arr[i], arr[i - 1])
            
            while maxVal > minVal * 2:
                cnt += 1
                minVal *= 2
        
        print(cnt)