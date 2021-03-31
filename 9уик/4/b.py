lst = [] 
n = int(input()) 
lst = input().split()
for i in range(len(lst)) : 
    if(int(lst[i]) % 2 == 0):
        print(lst[i], end=' ')