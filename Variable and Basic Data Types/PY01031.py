import sys

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_base(num, base):
    if num == 0:
        return "0"

    res = []
    while num > 0:
        res.append(DIGITS[num % base])
        num //= base
    
    return "".join(reversed(res))
    
if __name__ == '__main__':
    
    data = sys.stdin.read().split()
    test = int(data[0])
    idx = 1
    for _ in range(test):
        n = int(data[idx])
        base = int(data[idx + 1])
        
        idx += 2
        
        print(convert_base(n, base))
        