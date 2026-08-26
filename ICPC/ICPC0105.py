if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        s = input()
        res = ""
        for c in s:
            if c.isalpha(): res += " "
            else: res += c
        
        arr = list(map(int, res.split()))
        print(max(arr))