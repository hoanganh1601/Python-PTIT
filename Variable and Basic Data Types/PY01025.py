if __name__ == '__main__':
    num = input()
    
    res = ""
    cnt = 0
    
    for i in range(len(num) - 1, -1, -1):
        if cnt < 3:
            cnt += 1
            res += num[i]
        else:
            cnt = 1
            res += "," + num[i]
    
    tmp = reversed(res)
    print("".join(tmp))