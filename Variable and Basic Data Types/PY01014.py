if __name__ == '__main__':
    a, k, n = map(int, input().split())
    if a >= n:
        print(-1)
    else:
        # limit = n - a
        # print(limit)
        # first = (a // k + 1) * k
        first = (a + k - 1) // k * k
        # print(first)
        
        if(first > n or first == a):
            print(-1)
        else:
            for i in range(first, n + 1, k):
                print(i - a, end = " ")