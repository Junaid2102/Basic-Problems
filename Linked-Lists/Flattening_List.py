'''
Given a linked list where every node represents a linked list and contains two pointers of its type:

Pointer to next node in the main list (we call it ‘right’ pointer in the code below)
Pointer to a linked list where this node is headed (we call it the ‘down’ pointer in the code below).

Input:    5 -> 10 -> 19 -> 28
          |    |     |      |
          V    V     V      V
          7    20    22     35
          |          |      |
          V          V      V
          8          50     40
          |                 |
          V                 V
          30                45

Output: 5->7->8->10->19->20->22->28->30->35->40->45->50
'''

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return None
    dummy = Node(0, None, head, None)
    stack, p = [], dummy
    while p.next:
        if p.next.child:
            if p.next.next:
                stack.append(p.next.next)
            p.next.child.prev = p.next
            p = p.next.child
            p.next = stack[-1] if stack else None
        else:
            p = p.next
    dummy.next.prev = None
    return dummy.next


head = Node(1, None, Node(2, None, Node(3, None, Node(4, None, None, None), Node(5, None, None, None)), None), None)
flatten_head = flatten(head)
print("Hardcoded input: ")
p = flatten_head
while p:
    print(p.val)
    p = p.next
