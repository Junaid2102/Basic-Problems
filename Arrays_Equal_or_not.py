'''
    Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said
    to be equal if both of them contain same set of elements, arrangements (or permutation) of elements
    may be different though.
    Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
    Input:
        N = 5
        A[] = {1,2,5,4,0}
        B[] = {2,4,5,0,1}
    Output: 1
    Explanation: Both the array can be rearranged to {0,1,2,4,5}
'''

def check_two_arrays(arr1, arr2):
  n1 = len(arr1)
  n2 = len(arr2)
  if n1 == n2:
    arr1.sort()
    arr2.sort()
    for i in range(n1):
      if arr1[i] != arr2[i]:
        return 0
  return 1


arr = [5, 6, 8, 9]
arr2 = [9, 8, 5, 6]
print(check_two_arrays(arr,arr2))
