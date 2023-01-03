'''
    Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
    Note:
      If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the last subarray
      (irrespective of its size). You shouldn't return any array, modify the given array in-place.
    Input:
      N = 5, K = 3
      arr[] = {1,2,3,4,5}
    Output: 3 2 1 5 4
    Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
'''

def reverse_sub_array(arr, n, k):
  i = 0
  while i < n:
    j = min(i+k-1, n-1)
    arr[i:j+1] = reversed(arr[i:j+1])
    i = j+1
  return arr

arr = [5, 6, 8, 9]
n = len(arr)
k = 3
print(reverse_sub_array(arr, n, k))