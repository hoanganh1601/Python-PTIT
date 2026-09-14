import sys

if __name__ == '__main__':
    data = sys.stdin.read().split()
    
    idx = 0
    while idx < len(data):
        a, b, c, d = map(int, data[idx : idx + 4])
        idx += 4
        
        if a == 0 and b == 0 and c == 0 and d == 0:
            break
        
        steps = 0
        while not (a == b == c == d):
            a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
            steps += 1
        print(steps)
        