class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posMap={}
        self.nums=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.posMap:
            self.nums.append(val)
            self.posMap[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.posMap:
            idx = self.posMap[val]
            last = self.nums[-1]
            self.posMap[last] = idx
            self.nums[idx] = last
            self.nums.pop()
            self.posMap.pop(val, 0)
            return True
        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums)-1)]
