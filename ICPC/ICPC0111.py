if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n, d = map(int, input().split())
        arr = list(map(int, input().split()))
        
        for i in range(d, n):
            print(arr[i], end = " ")
        
        for i in range(d):
            print(arr[i], end = " ")
        
        print()