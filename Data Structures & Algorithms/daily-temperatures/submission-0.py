class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

      
        new =[]
        for left in range(len(temperatures)):
            index=0
            for right in range(left+1,len(temperatures)):
                if temperatures[left] < temperatures[right]:
                    index = right-left
                    break
                    # print(left)
            new.append(index)   
                
        
        return new
            


        