def check(s, t):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(t[i]) - ord(t[i - 1])):
            return False
    return True

if __name__ == '__main__':
    test = int(input())
    
    for _ in range(test):
        s = input()
        t = s[::-1]
        if(check(s, t)): print("YES")
        else: print("NO")