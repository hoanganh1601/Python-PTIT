import sys

memo = {1: 1}
def init():
    for i in range(2, 101):
        cur = i
        cnt = 1
        while cur != 1:
            if cur % 2 == 0:
                cur //= 2
            else:
                cur = cur * 3 + 1
            cnt += 1
        memo[i] = cnt 

if __name__ == '__main__':
    init()
    data = sys.stdin.read().split()
    for x in data:
        if x == '0':
            break
        print(memo[int(x)])