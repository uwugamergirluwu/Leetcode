class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        first = None
        if self.empty():
            return None
        for i in range(len(self.stack)-1, -1, -1):
            if i==0:
                first = self.stack.pop()
            else:
                self.temp_stack.append(self.stack.pop())
        for i in range(len(self.temp_stack)-1, -1, -1):
            self.stack.append(self.temp_stack.pop())
        return first

    def peek(self):
        """
        :rtype: int
        """
        first = None
        if self.empty():
            return None
        for i in range(len(self.stack)-1, -1, -1):
            if i==0:
                first = self.stack[i]
            else:
                self.temp_stack.append(self.stack.pop())
        for i in range(len(self.temp_stack)-1, -1, -1):
            self.stack.append(self.temp_stack.pop())
        return first

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()