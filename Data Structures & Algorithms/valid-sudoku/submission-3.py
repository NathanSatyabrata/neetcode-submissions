class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        col = [set() for c in range(len(board))]
        row = [set() for c in range(len(board))]
        sBox = [set() for c in range(len(board))]

        minLimitBox = 0

        for i in range(len(board)):
            if i == 3 or i == 6:
                minLimitBox += 3

            box = minLimitBox

            for j in range(len(board[i])):
                # check if digit is between 1-9
                if isinstance(board[i][j], int):
                    if not 1 <= board[i][j] <= 9:
                        return False
                
                if j == 3 or j == 6:
                    box += 1
                
                # duplicate check
                if board[i][j] != ".":
                    if (board[i][j] in col[j] or board[i][j] in row[i] or board[i][j] in sBox[box]):
                        return False
                    
                    col[j].add(board[i][j])
                    row[i].add(board[i][j])
                    sBox[box].add(board[i][j])

        return True




                
        