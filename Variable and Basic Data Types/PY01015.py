def check(arr):
    limit = len(arr)
    for i in range(1, limit):
        if arr[i] < arr[i - 1]: return False
    return True        

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        arr = input()
        
        if check(arr): print("YES")
        else: print("NO")
        
    
        