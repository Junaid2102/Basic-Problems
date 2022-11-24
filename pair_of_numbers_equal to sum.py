arr = list(map(int, input("Enter the array elements: ").split()))
sum = int(input("Enter the sum: "))
size = len(arr)
out = []
count = 0
for i in range(0, size):
    for j in range(i+1, size):
        out.clear()         # To clear the list
        if arr[i]+arr[j] == sum:
            out.append(arr[i])
            out.append(arr[j])
            print(out)
            count += 1

print("The count of pair is: ", count)
