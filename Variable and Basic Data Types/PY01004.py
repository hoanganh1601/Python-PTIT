# from math import *
import math

def phi(num):
    res = num
    len = math.isqrt(num)
    for i in range(2, len + 1):
        if(num % i == 0):
            res -= res // i
            while(num % i == 0):
                num //= i
    
    if(num > 1): res -= res // num
    return res

def checkPrime(num):
    if(num <= 1): return False
    elif(num == 2 or num == 3): return True
    elif(num % 2 == 0 or num % 3 == 0): return False
    else: 
        len = math.isqrt(num)
        for i in range(5, len + 1, 6):
            if(num % i == 0 or num % (i + 2) == 0):
                return False
    return True

if __name__ == '__main__':
    test = int(input())
    for i in range(1, test + 1):
        n = int(input())
        k = phi(n)
        
        if(checkPrime(k)): print("YES")
        else: print("NO")