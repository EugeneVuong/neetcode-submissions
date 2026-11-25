class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, rowVal in enumerate(board):
            rowMap = set()
            for j, colVal in enumerate(board[i]):
                if board[i][j] == ".":
                    continue # Skip Parts of the Board (That Is Not a Number)
                
                if board[i][j] in rowMap:
                    return False
                
                rowMap.add(board[i][j])
        
        for i, rowVal in enumerate(board):
            colMap = set()
            for j, colVal in enumerate(board[i]):
                if board[j][i] == ".":
                    continue # Skip Parts of the Board (That Is Not a Number)
                
                if board[j][i] in colMap:
                    return False
                
                colMap.add(board[j][i])
        
        for square in range(9):
            squareMap = set()
            for i in range(3):
                for j in range(3):
                    
                    
                    indexI = (square//3) * 3 + i
                    indexJ = (square % 3) * 3 + j
                    if board[indexI][indexJ] == ".":
                        continue

                    if board[indexI][indexJ] in squareMap:
                        return False
                    
                    squareMap.add(board[indexI][indexJ])

                
        return True