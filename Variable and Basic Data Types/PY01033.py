import math

if __name__ == '__main__':
    left, right = map(int, input().split())
    
    for i in range(left, right - 1):
        for j in range(i + 1, right):
            for k in range(j + 1, right + 1):
                if math.gcd(i, j) == 1 and math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
                    print(f"({i}, {j}, {k})")