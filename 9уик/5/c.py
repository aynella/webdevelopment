def xor(x, y):
    if( x == y):
        return False
    else:
        return True
x, y = map(int, input().split())
print(int(xor(x, y)))