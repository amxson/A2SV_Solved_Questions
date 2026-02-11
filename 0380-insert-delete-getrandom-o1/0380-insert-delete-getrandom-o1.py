class RandomizedSet:

    def __init__(self):
        self.dictt = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        x = self.dictt.get(val,-1)
        if x == -1:
            self.dictt[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

        

    def remove(self, val: int) -> bool:
        x = self.dictt.get(val,-1)
        if x == -1:
            return False
        else:
            y = self.arr[-1]
            index = self.dictt[val]
            self.arr[index] = y
            self.dictt[y] = index
            self.arr.pop()
            del self.dictt[val]
            return True

        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()