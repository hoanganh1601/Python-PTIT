def checkLuckyNumber(num):
    if num[0] != '6':
        return False
    
    if "888" in num:
        return False
    
    for c in num:
        if c != '6' and c != '8':
            return False
    
    return True

if __name__ == '__main__':
    num = input()
    if checkLuckyNumber(num):
        print('YES')
    else:
        print('NO') 