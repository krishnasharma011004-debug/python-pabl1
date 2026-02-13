class Solution9:
    def isSubset(self, a, b):
        from collections import Counter
        
        countA = Counter(a)
        countB = Counter(b)
        
        for key in countB:
            if countB[key] > countA.get(key, 0):
                return False
        
        return True
