'''
Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from
the given list (if exists).
Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.
Input:
    LinkedList: 2->2->4->5
Output: 2 4 5
Explanation: In the given linked list 2 -> 2 -> 4 -> 5, only 2 occurs more than 1 time.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_Duplicate(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def build_linkedlist(input_list):
    head = ListNode(input_list[0])
    curr = head
    for i in range(1, len(input_list)):
        curr.next = ListNode(input_list[i])
        curr = curr.next
    return head

user_input = input("Do you want to use input linked list(y/n)? ")
if user_input.lower() == "y":
    input_list = list(map(int, input("Enter elements of the linked list seperated by sapce: ").strip().split()))
    head = build_linkedlist(input_list)
else:
    head = build_linkedlist([1, 2, 2, 4, 5, 6])

remove_Duplicate(head)
while head:
    print(head.val, end="")
    head = head.next