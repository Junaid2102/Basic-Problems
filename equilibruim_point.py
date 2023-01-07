'''
    Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array.
    Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements
    after it.
    Input:
      n = 5
      A[] = {1,3,5,2,2}
    Output: 3
    Explanation:  equilibrium point is at position 3 as elements before it (1+3) = elements after it (2+2).
'''


def equ_point(arr, n):
  left_sum = 0
  right_sum = sum(arr)
  for i in range(0, n):
    right_sum -= arr[i]
    if left_sum == right_sum:
      return i + 1    # We plus one because of position otherwise index would be return because index starts with 0
    left_sum += arr[i]
  return -1



arr = list(map(int, input().split()))
size = len(arr)
print(equ_point(arr, size))