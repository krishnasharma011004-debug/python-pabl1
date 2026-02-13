class Solution:
    def median(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        arr = []
        for i in range(r):
            for j in range(c):
                arr.append(matrix[i][j])

        arr.sort()

        return arr[(r * c) // 2]
