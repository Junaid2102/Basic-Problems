'''
    Given a array of N strings, find the longest common prefix among all strings present in the array.
    Input:
      N = 4
      arr[] = {geeksforgeeks, geeks, geek, geezer}
    Output: gee
    Explanation: "gee" is the longest common prefix in all the given strings.
'''

# Method 1
def longest_common(arr):
  if not arr:
    return ""
  longest_common = arr[0]
  for i in range(1, len(arr)):
    j = 0
    while j < len(longest_common) and j < len(arr[i]) and longest_common[j] == arr[i][j]:
      j+=1
    longest_common = longest_common[:j]
  return longest_common

# Method 2
def common_prefix(arr):
  if not arr:
    return ""
  return divide_and_conquer(arr, 0, len(arr)-1)

def divide_and_conquer(arr, low, high):
  if low == high:
    return arr[low]
  mid = (low + high) // 2
  left_common = divide_and_conquer(arr, low, mid)
  right_common = divide_and_conquer(arr, mid + 1, high)
  i = 0
  while i < len(left_common) and i < len(right_common) and left_common[i] == right_common[i]:
    i += 1
  return left_common[:i]


arr = list(input().split())
print(common_prefix(arr))
print(longest_common(arr))