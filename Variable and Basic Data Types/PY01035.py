if __name__ == '__main__':
    s = input()
    n = len(s)
    
    addZero = (3 - n % 3) % 3
    # print(addZero)
    s = "".join(["0"] * addZero) + s
    res = []
    for i in range(0, n + addZero, 3):
        tmp = 0
        k = 1
        for j in range(i + 2, i - 1, -1):
            tmp += k * int(s[j])
            k *= 2
        res.append(str(tmp))
    
    print("".join(res))     