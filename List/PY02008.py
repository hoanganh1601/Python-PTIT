import math

primes = []
is_prime = [True] * 10001 

def init():
    primes.append(0)
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, math.isqrt(10000)):
        if is_prime[i]:
            for j in range(i * i, 10000, i):
                is_prime[j] = False
    
    for i in range(10001):
        if is_prime[i]:
            primes.append(i)

if __name__ == '__main__':
    init()

    n, x = map(int, input().split())
    arr = []
    for i in range(n + 1):
        arr.append(x + primes[i])
        x += primes[i]
    
    # res = " ".join(map(str, arr))
    # print(type(res))
    print(" ".join(map(str, arr)))