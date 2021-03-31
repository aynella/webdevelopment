lst = [] 
n = int(input()) 
cnt = 0
lst = input().split()
for i in range(len(lst)) : 
    if(int(lst[i]) > 0):
        cnt += 1
print(cnt)