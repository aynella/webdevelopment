n = int(input())
lst = list(map(int, input().split()))
answer = "NO"
for i in range(1, n):
    if (lst[i] * lst[i-1]) > 0:
        answer = "YES"
print(answer)