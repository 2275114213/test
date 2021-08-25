class Solution(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        self.stack1.append(value)

    def deleteHead(self):
        if not self.stack2:
            if self.stack1:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            else:
                return -1
        return self.stack2.pop()


res = Solution()
res.appendTail("a")
res.appendTail("b")
res.appendTail("c")
dad = res.deleteHead()
print(dad)
