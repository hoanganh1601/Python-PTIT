def check(num):
    sum = int(num[0])
    for i in range(1, len(num)):
        if abs(ord(num[i]) - ord(num[i - 1])) != 2:
            return False
        sum += int(num[i])
    return sum % 10 == 0
    
if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        num = input()
        if check(num):
            print("YES")
        else:
            print("NO")