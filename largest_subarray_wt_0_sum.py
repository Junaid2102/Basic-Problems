'''
    Given an array having both positive and negative integers. The task is to compute the length of the largest subarray
    with sum 0.
    Input:
      N = 8
      A[] = {15,-2,2,-8,1,7,10,23}
    Output: 5
    Explanation: The largest subarray with sum 0 will be -2 2 -8 1 7.
'''


def largest_subarray(arr):
  hash_map = {}
  max_length = 0
  total_sum = 0
  for i, j in enumerate(arr):
    total_sum += j
    if total_sum in hash_map:
      max_length = max(max_length, i - hash_map[total_sum])
    else:
      hash_map[total_sum] = i
  return max_length




arr = list(map(int, input().split()))
size = len(arr)
print(largest_subarray(arr))