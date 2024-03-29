class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.map[val] = len(self.data)
            self.data.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            ind = self.map[val]
            last = self.data[-1]
            self.data[ind] = last
            self.map[last] = ind
            self.data.pop()
            #self.map.pop(val)
            del self.map[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.data)
         


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()