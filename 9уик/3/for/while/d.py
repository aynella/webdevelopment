n = int(input())
while True:
    if n == 1: 
        print('YES')
        break
    elif n & 1:
        print('NO')
        break
    n >>= 1