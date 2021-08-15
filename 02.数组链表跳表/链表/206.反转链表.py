"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


num = [1, 2, 3, 4, 5]
head = ListNode(1)
p = head
for i in range(1, len(num)):
    p.next = ListNode(num[i])
    p = p.next

res = Solution().reverseList(head)
print(res.next.val)