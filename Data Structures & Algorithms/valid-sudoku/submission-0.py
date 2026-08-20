'''
problem: check if theres dupes in rows, cols, and 3x3 grids (first 3 elements of each list in the list)
to do: 
make a set for every row, if theres a dupe, return False.
make a set for every col, if theres a dupe, return False.
make a set for every 3x3, if theres a dupe, return False
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowset = set()
            for num in row:
                if num == ".":
                    continue
                elif num in rowset:
                    return False
                else:
                    rowset.add(num)
    
        for col in range(len(board)):
            colset = set()
            for row in range(len(board)):
                num = board[row][col]
                if num == ".":
                    continue
                elif num in colset:
                    return False
                else:
                    colset.add(num)
        squares = collections.defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in squares[(row//3, col//3)]:
                    return False
                else:
                    squares[(row//3, col//3)].add(board[row][col])
        return True
            
        
            

        


