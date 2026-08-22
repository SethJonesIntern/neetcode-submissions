class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        squares = defaultdict(list)
        #Check Rows
        for i in range(9):
            row = {}
            col = {}
            for j in range(9):
                if board[i][j] != "." :

                    #Rows
                    if board[i][j] not in row:
                        row[board[i][j]] = board[i][j];
                    else: return False


                    #Squares

                    if board[i][j] not in squares[(i//3 , j//3)]:
                        squares[(i//3 , j//3)].append(board[i][j])
                    else: return False



                #Cols
                if board[j][i] != ".":
                    if board[j][i] not in col:
                        col[board[j][i]] = board[j][i];
                    else: return False
                
                





        return True
        