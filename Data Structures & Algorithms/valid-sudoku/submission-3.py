class Solution:
    rows = 9
    cols = 9

    valid_digits = list(range(10))

    subbox_rows = 3
    subbox_cols = 3

    @staticmethod
    def isValuesUnique(board: List[List[str]]) -> bool:
        # set is enough here, instead of hash map
        is_visited = set()

        rows_len = len(board)
        cols_len = len(board[0])

        for i in range(rows_len):
            for j in range(cols_len):
                val = board[i][j]

                if val == ".":
                    continue

                val = int(val)

                if val not in Solution.valid_digits:  # valid digits (0 - 9)
                    print("[unique val checker] Number not in range", val)
                    return False

                if val in is_visited:
                    return False
                else:
                    is_visited.add(val)

        return True

    @staticmethod
    def isRowValid(row: List[str]) -> bool:
        return Solution.isValuesUnique([row])

    @staticmethod
    def isColValid(col: List[str]) -> bool:
        return Solution.isRowValid(col)

    @staticmethod
    def isRowsValid(board: List[List[str]]) -> bool:
        for row_idx in range(Solution.rows):
            if not Solution.isRowValid(board[row_idx]):
                print("row not unique : ", board[row_idx])
                return False
        return True

    @staticmethod
    def getCols(board: List[List[str]]) -> List[List[str]]:
        row = [""] * 9
        cols = [row.copy() for _ in range(9)]

        rows_len = len(board)
        cols_len = len(board[0])  # Todo don't use magic number

        for i in range(rows_len):
            for j in range(cols_len):
                cols[j][i] = board[i][j]

        return cols

    @staticmethod
    def isColsValid(board: List[List[str]]) -> bool:
        cols = Solution.getCols(board)

        for col in cols:
            if not Solution.isColValid(col):
                print("cols not unique : ", col)
                return False

        return True

    @staticmethod
    def is_sub_box_valid(sub_box: List[List[str]]) -> bool:
        return Solution.isValuesUnique(sub_box)

    @staticmethod
    def isSubboxesValid(board: List[List[str]]) -> bool:
        rows_len = len(board)
        cols_len = len(board[0])

        for i in range(0, rows_len - 3 - 1, 3):
            for j in range(0, cols_len - 3 - 1, 3):
                print(f"Checking sub box ({i}, {j})")
                array = []
                for x in range(3):
                    for y in range(3):
                        array.append(board[i + x][j + y])
                print(array)
                if not Solution.isValuesUnique([array]):
                    print(
                        f"sub-box not valid : ({i, j}) -> ({i + 2, j + 2})",
                    )
                    return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            Solution.isRowsValid(board)
            and Solution.isColsValid(board)
            and Solution.isSubboxesValid(board)
        )
