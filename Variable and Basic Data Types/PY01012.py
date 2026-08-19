if __name__ == '__main__':
    a = input()
    b = input()
    pos = int(input())
    
    c = a[:pos - 1] + b + a[pos - 1:]
    print(c)