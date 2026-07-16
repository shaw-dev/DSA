class TrieNode:
    def __init__(self):
        self.children = {} #when u add dog, this adds, "d" then"o"" and so on
        self.isword = False


class PrefixTree:

    def __init__(self):
       
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr= self.head 
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr = curr.children[ch] 
        curr.isword= True
        



    def search(self, word: str) -> bool:
        curr= self.head 
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch] 
        if curr.isword is True:
            return True
        return False

           

    def startsWith(self, prefix: str) -> bool:

        curr=self.head
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr= curr.children[ch]
        return True
        
        