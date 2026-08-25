class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash = defaultdict(set)
        colhash = defaultdict(set)
        hash3 = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                elif (board[row][col] in rowhash[row] or
                board[row][col] in colhash[col] or
                board[row][col] in hash3[(row//3,col//3)]):
                    return False
                else:
                    rowhash[row].add(board[row][col])
                    colhash[col].add(board[row][col])
                    hash3[(row//3,col//3)].add(board[row][col])
        return True