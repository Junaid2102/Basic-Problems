'''
Write a program to print third largest in an array
'''

arr = list(map(int, input("Enter the array: ").split()))
largest = 0
second_largest = 0
third_largest = 0

for i in range(0, len(arr)):
    if arr[i] > largest:
        third_largest = second_largest
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest:
        third_largest = second_largest
        second_largest = arr[i]
    elif arr[i] > third_largest:
        third_largest = arr[i]

print("The third largest is ", third_largest)