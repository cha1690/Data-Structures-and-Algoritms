class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue= collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        q=self.queue
        q.append(x)
        for _ in range(len(q)-1):
            q.append(q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue:
            return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue:
            return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue)==0