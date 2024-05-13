# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, newVal):
        end = ListNode(newVal)
        n = self
        while n.next:
            n = n.next
        n.next = end


def deleteDuplicates(head):
    if head == None:
        return

    dummy = ListNode(0)
    dummy.next = head
    current_node = head
    prev_node = dummy

    while (current_node):
        if current_node.next and current_node.val == current_node.next.val:
            while current_node.next and current_node.val == current_node.next.val:
                current_node = current_node.next
            prev_node.next = current_node

        prev_node = prev_node.next
        current_node = current_node.next

    return dummy.next


head = [1, 1, 2, 3, 3]
a = ListNode(head[0])
for i in range(1, len(head)):
    a.append(head[i])

# b = ListNode(1)
# b.next = ListNode(1)
# b.next.next = ListNode(2)

# node = a

c = deleteDuplicates(a)

print(c.val)
while c.next:
    c = c.next
    print(c.val)
