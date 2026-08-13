if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        s = input()
        x1 = s[:2]
        x2 = s[-2:]
        if(x1 == x2): print("YES")
        else: print("NO")