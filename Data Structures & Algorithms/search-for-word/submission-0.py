class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        x = len(board)
        y = len(board[0])
        
    
        def find( i,j,idx):
            rows = len(board)
            cols = len(board[0])
            if idx == len(word):
                return True
            if (i<0 or i >=rows or j<0 or j>=cols or board[i][j]!=word[idx]):
                return False
            

            temp = board[i][j]
            board[i][j] = "$"
            found = (find(i+1,j,idx+1) or find(i,j+1,idx+1) 
            or find(i-1, j , idx+1) or find(i,j-1,idx+1))


            board[i][j]= temp
            return found
        for i in range(x):
            for j in range(y):
                if board[i][j] == word[0] :
                    if find(i,j,0):
                        return True
                
        return False
