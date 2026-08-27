if __name__ == '__main__':
    test = int(input())
    
    for _ in range(test):
        n = int(input())
        arr = list(map(int, input().split()))
        
        val1, val2, val3 = arr[0], int(-1e9), int(-1e9)
        
        for i in range(1, n):
            if val1 < arr[i]:
                val3 = val2
                val2 = val1
                val1 = arr[i]
            elif val2 < arr[i]:
                val3 = val2
                val2 = arr[i]
            elif val3 < arr[i]:
                val3 = arr[i]
        
        print(val1 + val2 + val3)