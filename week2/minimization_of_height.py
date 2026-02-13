class Solution2:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k
        
        for i in range(n - 1):
            min_val = min(smallest, arr[i + 1] - k)
            max_val = max(largest, arr[i] + k)
            
            if min_val < 0:
                continue
            
            ans = min(ans, max_val - min_val)
        
        return ans
