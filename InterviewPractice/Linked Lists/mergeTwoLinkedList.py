""""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].

""""

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    res = []
    while l1 != None and l2 != None:
        if l1.value <= l2.value:
            res.append(l1.value)
            l1 = l1.next
        else:
            res.append(l2.value)
            l2 = l2.next
    while l1 is not None:
        res.append(l1.value)
        l1 = l1.next

    while l2 is not None:
        res.append(l2.value)
        l2 = l2.next
    return res

