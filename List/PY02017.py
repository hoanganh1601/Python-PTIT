if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n = int(input())
        arr = list(map(int, input().split()))
        dict = {}
        
        for num in arr:
            dict[num] = dict.get(num, 0) + 1
        
        for num, freq in dict.items():
            if freq % 2 == 1:
                print(num)
                break