arr = list(map(int, input().split()))
size = len(arr)

for i in range(arr[0], arr[-1]+1):
    if i not in arr:
        print(i)
