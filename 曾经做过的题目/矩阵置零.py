class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows_to_zero = set()
        cols_to_zero = set()

        # 第一次遍历，记录需要置零的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        # 第二次遍历，根据记录将行和列置零
        for i in range(m):
            for j in range(n):
                if i in rows_to_zero or j in cols_to_zero:
                    matrix[i][j] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
    Do not return anything, modify matrix in-place instead.
    """

        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and matrix[i][j] == 0:
                for r in range(m):
                if matrix[r][j] == 0:
                continue
        matrix[r][j] = 0
        visited.add((r, j))
        for c in range(n):
            if matrix[i][c] == 0:
                continue
        matrix[i][c] = 0
        visited.add((i, c))
        visited.add((i, j))
        return matrix
