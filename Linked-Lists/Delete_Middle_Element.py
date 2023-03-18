'''
Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then
linked list should be modified to 1->2->4->5. If there are even nodes, then there would be two middle nodes, we need to
delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to
1->2->3->5->6.
If the input linked list is NULL or has 1 node, then it should return NULL
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def DeletemiddleNode(head):
    slow_ptr = fast_ptr = head
    prev = None
    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        prev = slow_ptr
        slow_ptr = slow_ptr.next
    prev.next = slow_ptr.next

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
    head = build_linkedlist([1, 2, 3 , 4, 5, 6])

DeletemiddleNode(head)
while head:
    print(head.val, end="")
    head = head.next