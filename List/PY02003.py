hamming_numbers = []
hamming_map = {}
limit = 10**18

def init():
    # Generate all combinations of 2^i * 3^j * 5^k <= 10^18
    for i in range (61):
        for j in range(39):
            for k in range(27):
                val = (2 ** i) * (3 ** j) * (5 ** k)
                if val <= limit:
                    hamming_numbers.append(val)
    
    hamming_numbers.sort()
    i = 1
    for x in hamming_numbers:
        hamming_map[x] = i
        i += 1

if __name__ == '__main__':
    init()
    
    test = int(input())
    for _ in range(test):
        n = int(input())
        if n in hamming_map:
            print(hamming_map[n])
        else:
            print("Not in sequence")        