class MinStack:

    def __init__(self):
        self.shelf=[]
        self.new=[]

    def push(self, val: int) -> None:
        self.shelf.append(val)
        if not self.new:
            self.new.append(val)
        else:
            last = self.new[-1]
            self.new.append(min(last,val))


        

    def pop(self) -> None:
        self.shelf.pop()
        self.new.pop()
        

    def top(self) -> int:
        return self.shelf[-1]
        

    def getMin(self) -> int:

        return self.new[-1]



        
