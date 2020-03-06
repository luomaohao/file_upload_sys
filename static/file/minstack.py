class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top=-1
        self.data=[]
        

    def push(self, x: int) -> None:
        self.top+=1
        self.data.append(x)
        

    def pop(self) -> None:
        if len(self.data):
            self.top-=1;
            

    def top(self) -> int:
        return self.data[self.top]

    def getMin(self) -> int:
        min=self.data[self.top]
        for i in self.data:
            if min>i:
                min = i
        return min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()