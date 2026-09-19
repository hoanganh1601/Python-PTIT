import math

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        num = input()
        arr = list(reversed(num))
        
        reversedNum = "".join(arr)
        
        if math.gcd(int(num), int(reversedNum)) == 1:
            print("YES")
        else:
            print("NO")
        