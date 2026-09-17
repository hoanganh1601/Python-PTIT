if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        num = input()
        suffix = num[len(num) - 2 : ]
        if suffix == '86':
            print("YES")
        else: 
            print("NO")