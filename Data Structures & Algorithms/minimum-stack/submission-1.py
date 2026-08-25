class MinStack:

    def __init__(self):
        self.working = []
        self.mins = []
        self.curMin = 0
        

    def push(self, val: int) -> None:
        #setting curmin if its first node pushed
        if len(self.working) == 0:
            self.curMin = val

        #add val
        self.working.append(val)

        #add curMin to mins
        if val < self.curMin:
            self.curMin = val
        
        self.mins.append(self.curMin)
        
        


    def pop(self) -> None:
        self.working.pop()
        self.mins.pop()

        if(len(self.mins) > 0):
            self.curMin = self.mins.pop()
            self.mins.append(self.curMin)


    def top(self) -> int:
        res = self.working.pop()
        self.working.append(res)
        return res

    def getMin(self) -> int:
        return self.curMin
