import math

LIMIT = 10500

is_prime = [True] * (LIMIT + 1)
primes = []
def init():
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, math.isqrt(LIMIT) + 1):
        if is_prime[i]:
            for j in range(i * i, LIMIT + 1, i):
                is_prime[j] = False
                
    for i in range(2, LIMIT + 1):
        if is_prime[i]:
            primes.append(i)

if __name__ == '__main__':
    init()
    
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    
    for num in arr:
        cur = 10**9
        for prime in primes:
            cur = min(cur, abs(prime - num))
        ans = max(ans, cur)
    
    print(ans)
    
    