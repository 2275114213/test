# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
#  push(x) —— 将元素 x 推入栈中。
#  pop() —— 删除栈顶的元素。
#  top() —— 获取栈顶元素。
#  getMin() —— 检索栈中的最小元素。
#
#
#
#
#  示例:
#
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  pop、top 和 getMin 操作总是在 非空栈 上调用。
#
#  Related Topics 栈 设计
#  👍 983 👎 0

from typing import *


# 两个栈
# class Solution(object):
#     def __init__(self):
#         self.stack1 = []
#         self.minstack = []
#
#     def push(self, value):
#         if not self.minstack or value <= self.minstack[-1]:
#             self.minstack.append(value)
#         self.stack1.append(value)
#
#     def pop(self):
#         value = self.stack1.pop()
#         if value == self.minstack[-1]:
#             self.minstack.pop()
#         return value
#
#     def top(self):
#         return self.stack1[-1]
#
#     def getMin(self):
#         return self.minstack[-1]

class Solution(object):
    def __init__(self):
        self.stack1 = []
        self.minstack = None

    def push(self, value):
        # 差值
        diff = value - self.stack1[-1]
        if diff < 0:
            self.minstack = diff
        self.stack1.append(diff)

    def pop(self):
        value = self.stack1.pop()
        if self.minstack<0:
            self.

    def top(self):
        return self.stack1[-1]

    def getMin(self):
        return self.minstack[-1]


minStack = Solution()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
