class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 上下翻转
        for x in range(int(n/2)):
            for y in range(n):
                matrix[x][y],matrix[~x][y] = matrix[~x][y],matrix[x][y]
        # 沿对角线翻转
        for x in range(n):
            for y in range(x):
                matrix[x][y],matrix[y][x] = matrix[y][x],matrix[x][y]