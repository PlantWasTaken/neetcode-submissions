class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_row = set()
            seen_col = set()
            seen_box = set()
            for j in range(9):
                # Row check
                if board[i][j] != ".":
                    if board[i][j] in seen_row: return False
                    seen_row.add(board[i][j])
                # Column check
                if board[j][i] != ".":
                    if board[j][i] in seen_col: return False
                    seen_col.add(board[j][i])
                # Box check
                box_r, box_c = 3 * (i // 3) + j // 3, 3 * (i % 3) + j % 3
                if board[box_r][box_c] != ".":
                    if board[box_r][box_c] in seen_box: return False
                    seen_box.add(board[box_r][box_c])
        return True