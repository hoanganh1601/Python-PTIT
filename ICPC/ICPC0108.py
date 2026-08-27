if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n = int(input())
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        cnt = 0
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                curSum = arr[i] + arr[left] + arr[right]
                if curSum == 0:
                    cnt += 1
                    left += 1
                    right -= 1
                elif curSum < 0:
                    left += 1
                else:
                    right -= 1
        
        print(cnt)