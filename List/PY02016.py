if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n = int(input())
        arr = list(map(int, input().split()))
        dict = {}
        
        for num in arr:
            dict[num] = dict.get(num, 0) + 1
        
        res, maxFreq = None, -1
        for num, freq in dict.items():
            if maxFreq < freq:
                maxFreq = freq
                res = num
        
        if maxFreq > n // 2:
            print(res)
        else:
            print("NO")