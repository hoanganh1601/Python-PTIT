if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        total = 0
        string = ""
        
        s = input()
        for c in s:
            if c.isdigit():
                total += int(c)
            else:
                string += c
        
        res = sorted(string)
        print(f"{"".join(res)}{total}")
    