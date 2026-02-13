class Solution:
    def median(self, matrix, r, c):
        arr = []
        for row in matrix:
            arr.extend(row)
        
        arr.sort()
        return arr[(r * c) // 2]
