import sys 

if __name__ == '__main__':
    data = sys.stdin.read().split()
    test = int(data[0])
    
    res = []
    for idx in range(1, test + 1):
        s = list(data[idx])
        n = len(s)
        
        # rightmost dip
        i = n - 2
        while i >= 0 and s[i] <= s[i + 1]:
            i -= 1
            
        if i < 0:
            res.append("-1")
            continue
        
        # swap -> best answer
        bestChar = '-1'
        j = -1
        
        for k in range(i + 1, n):
            if s[k] < s[i]:
                if s[k] > bestChar:
                    bestChar = s[k]
                    j = k
        
        s[i], s[j] = s[j], s[i]
        if s[0] == '0':
            res.append("-1")
        else:
            res.append("".join(s))
        
    print("\n".join(res))
        
        
        