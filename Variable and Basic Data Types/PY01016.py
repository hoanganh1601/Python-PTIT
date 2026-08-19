if __name__ == '__main__':
    test = int(input())
    
    for _ in range(test):
        s = input()
        
        length = len(s)
        for i in range(1, len(s), 2):
            print(s[i - 1] * int(s[i]), end = "")
        print()