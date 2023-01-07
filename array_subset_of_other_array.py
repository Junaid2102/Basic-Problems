'''
    Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[]
    or not. Both the arrays can be sorted or unsorted.
    Input:
      a1[] = {11, 1, 13, 21, 3, 7}
      a2[] = {11, 3, 7, 1}
    Output:
      Yes
    Explanation: a2[] is a subset of a1[]
'''

# Brute force
def is_subset(A1, A2):
  for i in A2:
    if i not in A1:
      return False
  return True

# Binary_Search_Technique

def subset(A1, A2):
  A1.sort()
  for i in A2:
    if not binary_search(A1, i):
      return False
  return True

def binary_search(A1, i):
  low = 0
  high = len(A1) - 1
  while low <= high:
    mid = (low + high) // 2
    if A1[mid] == i:
      return True
    elif A1[mid] < i:
      low = mid + 1
    else:
      high = mid - 1
  return False



arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
if is_subset(arr1, arr2) == True:
  print("YES")
else:
  print("NO")

if subset(arr1, arr2) == True:
  print("YES")
else:
  print("NO")