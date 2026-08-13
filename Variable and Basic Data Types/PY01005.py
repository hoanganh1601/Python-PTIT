if __name__ == '__main__':
    num = input()
    cnt47 = num.count('4') + num.count('7')
    
    if(cnt47 == 4 or cnt47 == 7): print("YES")
    else: print("NO")