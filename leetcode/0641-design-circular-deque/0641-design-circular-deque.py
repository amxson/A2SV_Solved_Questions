class MyCircularDeque:

    def __init__(self, k: int):
        self.deq = deque()
        self.k = k
        self.c = 0
        

    def insertFront(self, value: int) -> bool:
        if self.c<self.k:
            self.deq.appendleft(value)
            self.c +=1
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if self.c<self.k:
            self.deq.append(value)
            self.c +=1
            return True
        else:
            return False
        
        

    def deleteFront(self) -> bool:
        if self.c>0:
            self.deq.popleft()
            self.c -=1
            return True
        else:
            return False
        
        

    def deleteLast(self) -> bool:
        if self.c>0:
            self.deq.pop()
            self.c -=1
            return True
        else:
            return False
        
        

    def getFront(self) -> int:
        if self.c>0:
            return self.deq[0]
        else:
            return -1
        
        

    def getRear(self) -> int:
        if self.c>0:
            return self.deq[-1]
        else:
            return -1
        
        

    def isEmpty(self) -> bool:
        if self.c>0:
            return False
        else:
            return True
        
        

    def isFull(self) -> bool:
        if self.c==self.k:
            return True
        else:
            return False
        
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()