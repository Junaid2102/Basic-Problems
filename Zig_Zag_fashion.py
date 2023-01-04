'''
    Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array in a
    zig-zag fashion so that the converted array should be in the below form:
      arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n].
    Input:
      N = 7
      rr[] = {4, 3, 7, 8, 6, 2, 1}
    Output: 3 7 4 8 2 6 1
    Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1
'''


def zig_zag(arr):
  n = len(arr)
  for i in range(1, n):
    if (i % 2 == 1 and arr[i-1] > arr[i]) or (i % 2 == 0 and arr[i-1] < arr[i]):
      arr[i-1], arr[i] = arr[i], arr[i-1]
  return arr


arr = [4, 3, 7, 8, 6, 2, 1]
k = 3
print(zig_zag(arr))
