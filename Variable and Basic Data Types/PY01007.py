import math

if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        n, x, m = map(float, input().split())
        res = math.log(m / n, 1 + x / 100) # log(num, base)
        
        print(math.ceil(res))