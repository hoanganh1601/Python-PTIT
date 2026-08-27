def convert(num, p, q):
    res = ""
    for c in num:
        if int(c) == p:
            res += str(q)
        else:
            res += c
    return int(res)

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        p, q = map(int, input().split())
        tmp1 = min(p, q)
        tmp2 = max(p, q)
        
        s = input().strip()
        if s.count(' '): s, t = s.split()
        else: t = input()
        
        print(convert(s, tmp2, tmp1) + convert(t, tmp2, tmp1), convert(s, tmp1, tmp2) + convert(t, tmp1, tmp2))
        '''
        print(int(s.replace(tmp2, tmp1)) + int(t.replace(tmp2, tmp1)), end = " ")
        print(int(s.replace(tmp1, tmp2)) + int(t.replace(tmp1, tmp2)))
        '''
        