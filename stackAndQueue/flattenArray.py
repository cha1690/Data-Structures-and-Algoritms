class NestedIterator:
    def __init__(nestedList):
        self.stack=nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        while self.stack:
            element= self.stack[-1]
            if element.isInteger():
                return True
            self.stack.pop()
            for i in element.getList()[::-1]:
                self.stack.append(i)
        return False