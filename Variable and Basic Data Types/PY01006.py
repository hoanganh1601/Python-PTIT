def check(num):
    for x in num:
        if(x != '4' and x != '7'): return False
    return True

if __name__ == '__main__':
    
    test = int(input())
    for i in range(test):
        num = input()
        if(check(num)): print("YES")
        else: print("NO")
        
    