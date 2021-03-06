"""
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


# 暴力破解法
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         seen = set()
#         while head:
#             if head in seen:
#                 return True
#             else:
#                 seen.add(head)
#                 head = head.next
#         return False

# 快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


num = [1, 2, 3, 4, 5]
head = ListNode(1)
p = head
for i in range(1, len(num)):
    p.next = ListNode(num[i])
    p = p.next
p.next = head
Solution().hasCycle(head)
