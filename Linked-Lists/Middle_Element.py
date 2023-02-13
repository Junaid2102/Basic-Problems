'''
Auxiliary Given a singly linked list, find the middle of the linked list. For example, if the given linked list is
1->2->3->4->5 then the output should be 3. If there are even nodes, then there would be two middle nodes,
we need to print the second middle element.
For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow_ptr = fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr

# For hard coded input
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
result = middleNode(head)
print("Middle element is:", result.val)

# For user input
nodes = list(map(int, input("Enter the elements for linked list seperated by spaces: ").strip().split()))
head = ListNode(nodes[0])
curr = head
for i in range(1, len(nodes)):
    curr.next = ListNode(nodes[i])
    curr = curr.next
userresult = middleNode(head)
print("Middle element is: ", userresult.val)