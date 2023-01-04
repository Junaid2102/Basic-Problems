'''
    Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds
    to a given number S and return the left and right index(1-based indexing) of that subarray.

    In case of multiple subarrays, return the subarray indexes which comes first on moving from left to right.

    Input:
      N = 5, S = 12
      A[] = {1,2,3,7,5}
    Output: 2 4
    Explanation: The sum of elements from 2nd position to 4th position is 12.
'''

# Brute Force Approach


def find_subarray(A, N, S):
  for i in range(N):
    for j in range(i + 1, N + 1):
      if sum(A[i:j]) == S:
        return (i + 1, j)
  return (-1, -1)


# Window Sliding Approach

def subarray_find(A, N, S):
  l = 0
  r = 0
  window = A[0]
  # print(window)
  while r < N:
    if window > S:
      window -= A[l]
      #print(window)
      l += 1
    elif window < S:
      r += 1
      if r < N:
        window += A[r]
        #print(window)
    else:
        return (l+1, r+1)
  return(-1, -1)


arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
s = 18
print(find_subarray(arr, n, s))
print(subarray_find(arr, n, s))
