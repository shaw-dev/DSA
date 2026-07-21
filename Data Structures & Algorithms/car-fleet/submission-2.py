class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        new =[]
        new=[(i,j) for i,j in zip(position,speed)]

        new.sort(reverse=True)
        stack=[]

        for i,j in new:
            time = (target-i)/j
            stack.append(time)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)