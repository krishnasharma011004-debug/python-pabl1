class Solution1:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k - 1]
