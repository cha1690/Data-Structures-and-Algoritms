class Calls:
    def __init__(self):
        self.call=collections.deque()

    def ping(self,t):
        self.call.append(t)
        # append inserts items from the right
        while self.call[0] < 3000:
            self.call.popleft()
        return len(self.call)