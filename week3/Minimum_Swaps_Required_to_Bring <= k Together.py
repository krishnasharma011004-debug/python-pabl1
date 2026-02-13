class Solution:
    def minSwap(self, arr, n, k):
        
        count = 0
        for num in arr:
            if num <= k:
                count += 1
        
        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        for i in range(0, n - count):
            if arr[i] > k:
                bad -= 1
            if arr[i + count] > k:
                bad += 1
            
            ans = min(ans, bad)
        
        return ans
