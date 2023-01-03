'''
    Given a sorted array of size N and an integer K, find the position at which K is present
    in the array using binary search.
    Input:
        N = 5
        arr[] = {1 2 3 4 5}
        K = 4
    Output: 3
    Explanation: 4 appears at index 3.
'''

def binary_search(array, k):
  l = 0
  u = len(array) - 1;
  while l <= u:
    m = l + (u - l) // 2
    if array[m] == k:
      return m
    elif array[m] < k:
      l = m + 1
    else:
      u = m - 1
  return -1


arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 4
print(binary_search(arr, k))