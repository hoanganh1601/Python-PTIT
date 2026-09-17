if __name__ == '__main__':
    num = input().strip()
    
    cnt = 0
    while len(num) > 1:
        total = 0
        for c in num:
            total += ord(c) - ord('0')
        num = str(total)
        cnt += 1
    print(cnt)
    