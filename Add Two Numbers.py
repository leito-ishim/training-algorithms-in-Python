# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2) -> ListNode:
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummyHead = ListNode(0)
    curr = dummyHead
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        columnSum = l1Val + l2Val + carry
        carry = columnSum // 10
        newNode = ListNode(columnSum % 10)
        curr.next = newNode
        curr = newNode
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyHead.next


# print(addTwoNumbers(w1, w2))
print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
# print(addTwoNumbers([0], [0]))
# print(addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))

# def addTwoNumbers(l1, l2):
#     k = 1
#     rez1 = 0
#     rez2 = 0
#     for i in range(len(l1)):
#         rez1 = rez1 + int(l1[i]) * k
#         k *= 10
#     k = 1
#     for i in l2:
#         rez2 = rez2 + int(i) * k
#         k *= 10
#     rezult = [int(d) for d in str(rez1 + rez2)]
#     return rezult[::-1]
