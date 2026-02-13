class Solution7:
    def commonElements(self, A, B, C):
        i = j = k = 0
        n1, n2, n3 = len(A), len(B), len(C)
        result = []
        
        while i < n1 and j < n2 and k < n3:
            
            if A[i] == B[j] == C[k]:
                if not result or result[-1] != A[i]:
                    result.append(A[i])
                i += 1
                j += 1
                k += 1
            
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        
        return result if result else [-1]
