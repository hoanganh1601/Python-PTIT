fibo = [0] * 93

def init():
    fibo[1] = 1
    for i in range(2, 93):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    
if __name__ == "__main__":
    init()
    test = int(input())
    for _ in range(test):
        left, right = map(int, input().split())
        for i in range(left, right + 1):
            print(fibo[i], end = " ")
        print()