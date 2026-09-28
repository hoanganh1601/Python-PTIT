import sys

if __name__ == '__main__':
    data = sys.stdin.read().split()
    test = int(data[0])
    
    for i in range(1, test + 1):
        n = int(data[i])
        
        if n % 7 == 0:
            print(n)
            continue
        
        found = False
        for _ in range(1000):
            rev = int(str(n)[::-1])
            n += rev
            
            if n % 7 == 0:
                print(n)
                found = True
                break
        
        if not found:
            print(-1)               
            