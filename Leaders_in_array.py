'''
    Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader
    if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.
    Input:
      n = 6
      A[] = {16,17,4,3,5,2}
    Output: 17 5 2
    Explanation: The first leader is 17 as it is greater than all the elements to its right.
    Similarly, the next leader is 5. The right most element is always a leader so it is also included.
'''


def leaders_in_array(A, N):
  leaders =[]
  for i in range (0, N):
    for j in range(i+1, N):
      if A[i] < A[j]:
        break
      j = j+1
      if j == N:
        leaders.append(A[i])
  return leaders


arr = list(map(int, input().split()))
size = len(arr)
print(leaders_in_array(arr, size))
