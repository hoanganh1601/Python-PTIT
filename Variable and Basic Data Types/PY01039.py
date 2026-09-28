import sys

def check(num):
    if len(set(num)) != 2:
        return False
        
    for i in range(len(num) - 2):
        if num[i] != num[i + 2]:
            return False
            
    return True
    
if __name__ == '__main__':
    data = sys.stdin.read().split()
        
    test = int(data[0])
    for i in range(1, test + 1):
        if check(data[i]):
            print("YES")
        else:
            print("NO")