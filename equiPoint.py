n = int(input())
arr = list(map(int, input().split()))
print(arr)
flag = 0
if (n == 1):
    print("1")
else:
    for x in range(n):
        if (sum(arr[:x]) == sum(arr[x + 1:])):
            val = x
            flag = 1
    if (flag == 1):
        print(val + 1)
    else:
        print(-1)