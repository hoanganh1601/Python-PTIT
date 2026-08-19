if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        s = input()
        cnt = 1
        length = len(s)
        for i in range(1, len(s)):
            if(s[i] == s[i - 1]):
                cnt += 1
            else:
                print(f"{cnt}{s[i - 1]}", end = "")
                cnt = 1 
        
        print(f"{cnt}{s[length - 1]}")