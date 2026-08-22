'''
prob: see if theres dupes in rows, cols, and 3 by 3s.
to do: i can make 3 hashmaps that map rows/cols/3 by 3 (sections) to set vals.
if the val is ., skip, if dupe return false, else add it in.
for the 3 by 3s, the key can be found by making a grouping the 3x3 section into a subsection of a larger 3 by 3 section. meaning, each 3 by 3 sequence will be in r/3, c/3.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash = collections.defaultdict(set)
        colhash = collections.defaultdict(set)
        hash_3 = collections.defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                elif (board[row][col] in rowhash[row] 
                or board[row][col] in colhash[col] 
                or board[row][col] in hash_3[(row//3, col//3)]):
                    return False
                else:
                    rowhash[row].add(board[row][col])
                    colhash[col].add(board[row][col])
                    hash_3[(row//3, col//3)].add(board[row][col])
        return True


        