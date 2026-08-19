if __name__ == '__main__':
    
    P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    
    while(True):
        tmp = input().split()
        
        k = int(tmp[0])
        if(k == 0): break
        
        s = tmp[1]
        length = len(s)
        
        res = ""
        for char in s:
            res += P[(P.index(char) + k) % 28]
        
        print(res[::-1])
            
        