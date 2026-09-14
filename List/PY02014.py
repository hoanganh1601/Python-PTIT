import math

is_prime = [True] * 10001
primes = []
def init():
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, math.isqrt(10001)):
        if is_prime[i]:
            for j in range(i * i, 10001, i):
                is_prime[j] = False
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
    
    