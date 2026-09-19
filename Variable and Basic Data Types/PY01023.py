import math

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n = int(input())
        factors = []
        
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                cnt = 0
                while n % i == 0:
                    cnt += 1
                    n //= i
                factors.append(f"{i}^{cnt}")
        
        if n > 1:
            factors.append(f"{n}^{1}")

        if factors:
            print("1 * " + " * ".join(factors))
        else:
            print("1")