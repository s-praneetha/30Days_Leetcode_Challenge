class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [None]*9000

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val > 9000 or val < 0:
            index = val%9000
        else:
            index = val
        if self.set[index] is not None:
            return False
        else:
            self.set[index] = val
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val > 9000 or val < 0:
            index = val%9000
        else:
            index = val
        if self.set[index] is None:
            return False
        else:
            self.set[index] = None
            return True

        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        tmp = int(random.random()*9000)
        while self.set[tmp] == None:
            tmp = int(random.random()*9000)
        return self.set[tmp]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()