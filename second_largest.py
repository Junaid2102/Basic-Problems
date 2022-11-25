'''
Write a program to print second largest in an array
'''

arr = list(map(int, input("Enter the array: ").split()))
largest = 0
second_largest = 0
for i in range(0, len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest:
        second_largest = arr[i]

print("The third largest is ", second_largest)