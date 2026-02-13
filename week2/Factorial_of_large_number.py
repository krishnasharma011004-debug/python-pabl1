class Solution8:
    def factorial(self, N):
        result = 1
        for i in range(2, N + 1):
            result *= i
        return list(map(int, str(result)))
