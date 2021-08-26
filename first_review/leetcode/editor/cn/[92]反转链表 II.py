# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
#  提示：
#
#
#  链表中节点数目为 n
#  1 <= n <= 500
#  -500 <= Node.val <= 500
#  1 <= left <= right <= n
#
#
#
#
#  进阶： 你可以使用一趟扫描完成反转吗？
#  Related Topics 链表
#  👍 994 👎 0

from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        if left == right:
            return head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            print("===", next.val)
            print("@", cur.next.val, next.next.val)
            cur.next = next.next
            print("#", next.next.val, pre.next.val)
            next.next = pre.next
            pre.next = next

        # leetcode submit region end(Prohibit modification and deletion)
        pass


num = [1, 2, 3, 4, 5]
head = ListNode(1)
p = head
for i in range(1, len(num)):
    p.next = ListNode(num[i])
    p = p.next

res = Solution().reverseBetween(head, 2, 4)
