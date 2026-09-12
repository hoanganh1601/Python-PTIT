import sys

if __name__ == '__main__':
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        
        if n == 0:
            break
        
        numbers = []
        for _ in range(n):
            numbers.append(int(data[idx]))
            idx += 1
        
        minVal = min(numbers)
        maxVal = max(numbers)
        
        if minVal == maxVal:
            print("BANG NHAU")
        else:
            print(minVal, maxVal, sep = " ")
