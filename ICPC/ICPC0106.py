import math

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        base = int(input())
        s = input()
        
        if base == 2:
            print(s)
        else:
            k = int(math.log2(base))
            length = len(s)
            # print(length)
            tmp = (k - length % k) % k
            for _ in range(tmp):
                s = "0" + s

            res = ""
            
            for i in range(0, len(s), k):
                cnt = 0
                ok2 = 1
                for j in range(i + k - 1, i - 1, - 1):
                    cnt += (int(s[j]) * ok2)
                    ok2 *= 2
                
                # important (base = 16)
                if cnt < 10:
                    res += str(cnt)
                else:
                    res += chr(ord('A') + cnt - 10)
            
            print(res)
            
        
        