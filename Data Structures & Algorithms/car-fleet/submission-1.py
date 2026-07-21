class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=[]

        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        
        cars.sort(reverse=True)

        nfleets=0
        current=0

        for i,j in cars:
            time = (target-i)/j

            if time > current:
                nfleets+=1
                current=time
        return nfleets
        