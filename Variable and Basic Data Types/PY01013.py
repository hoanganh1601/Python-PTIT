import math

def gcd(a, b):
    if(not b): return a
    return gcd(b, a % b)

def sumDigit(num):
    total = 0
    while(num > 0):
        total += num % 10
        num //= 10
    return total

def checkPrime(num):
    if(num < 2): return False
    elif(num == 2 or num == 3): return True
    elif(num % 2 == 0 or num % 3 == 0): return False
    else:
        limit = math.isqrt(num)
        for i in range(5, limit + 1, 6):
            if(num % i == 0 or num % (i + 2) == 0): return False
    return True

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        a, b = map(int, input().split())
        k = gcd(a, b)
        
        if(checkPrime(sumDigit(k))): print("YES")
        else: print("NO")        
        