class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box = row // 3 * 3 + col // 3
                if val in rows[row] or val in cols[col] or val in boxs[box]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                boxs[box].add(val)
        return True