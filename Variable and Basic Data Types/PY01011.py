validNumbers = []
def init():
    queue = ['2', '4', '6', '8']   
    
    while queue:
        half = queue.pop(0)
        palidrome = half + half[::-1]
        validNumbers.append(int(palidrome))
        
        if(len(half) < 3):
            for nums in ['0', '2', '4', '6', '8']:
                queue.append(half + nums)
    
    validNumbers.sort()        


if __name__ == '__main__':
    init()
    test = int(input());
    
    for _ in range(test):
        n = int(input())
        for num in validNumbers:
            if(num >= n): break
            print(num, end = " ")
        print()