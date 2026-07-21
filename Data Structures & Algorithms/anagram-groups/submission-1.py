class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        track={}
        answer=[]
        for i in strs:
            newarray = [0]*26
            for char in i:
                index= ord(char)-ord("a") #this is the index
                newarray[index]+=1

            key = tuple(newarray)#this is the key or distinct word

            if key not in track:
                track[key]=[]
            track[key].append(i)#adding the right word to its distinct key
        answer = list(track.values())
        return answer

            
            


        