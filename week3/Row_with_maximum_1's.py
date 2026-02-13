class Solution:
    def rowWithMax1s(self, arr, n, m):
        max_row = -1
        max_count = 0
        
        for i in range(n):
            count = sum(arr[i])
            if count > max_count:
                max_count = count
                max_row = i
        
        return max_row
