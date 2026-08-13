if __name__ == '__main__':
    s = input()
    low, up = 0, 0
    
    for x in s:
        if(x.islower()): low += 1
    
    up = len(s) - low
    if(low < up): print(s.upper())
    else: print(s.lower())