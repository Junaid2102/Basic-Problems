'''
Delete the elements in a linked list whose sum is equal to zero
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_zerosum(head):
    dummy = ListNode(0)
    dummy.next = head
    curr, prev = head, dummy
    while curr:
        sum = 0
        while curr and sum + curr.val != 0:
            sum += curr.val
            curr = curr.next
        if not curr:
            break
        prev.next = curr.next
        curr = curr.next
    return dummy.next

def build_linkedlist(input_list):
    head = ListNode(input_list[0])
    curr = head
    for i in range(1, len(input_list)):
        curr.next = ListNode(input_list[i])
        curr = curr.next
    return head

user_input = input("Do you want to use input linked list(y/n)? ")
if user_input.lower() == "y":
    input_list = list(map(int, input("Enter the elements of the linked list separated by space: ").strip().split()))
    head = build_linkedlist(input_list)
else:
    head = build_linkedlist([1,2,-3,3,-2,2])

new_head = delete_zerosum(head)
print("The linked list after deleteion: ")
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next