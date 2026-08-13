test = int(input())
for i in range(1, test + 1) :
    num = int(input())
    k = 10
    while(k <= num):
        mod = num % k
        # print(mod)
        num -= mod
        if(mod >= k // 2):
            num += k 
        k *= 10
    print(num)
    