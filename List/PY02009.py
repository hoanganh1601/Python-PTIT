if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n = int(input())
        mp = {}
        for i in range(n):
            k = int(input())
            mp[k] = mp.get(k, 0) + 1
        
        sorted_item = sorted(mp.items(), key = lambda x : (-x[1], x[0]))
        
        print(sorted_item[0][0])
        