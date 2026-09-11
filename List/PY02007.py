import sys

input_data = sys.stdin.read().split()

res = set()
for i in range(10):
    num = int(input_data[i])
    res.add(num % 42)

print(len(res))