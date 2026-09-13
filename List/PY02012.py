import sys

if __name__ == '__main__':
    data = sys.stdin.read().split()

    n = int(data[0])
    arr = [int(x) for x in data[1:n + 1]]
    
    even_numbers = [x for x in arr if x % 2 == 0]
    odd_numbers = [x for x in arr if x % 2 == 1]
    
    even = sorted(even_numbers)
    odd = sorted(odd_numbers, reverse = True)
    
    i, j = 0, 0
    res = []
    for x in arr:
        if x % 2 == 0:
            res.append(even[i])
            i += 1
        else:
            res.append(odd[j])
            j += 1            
    
    print(*res)