class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        i = 1
        s = 2
        result = s

        count = 2
        while(count < n):
            temp = i
            result = i + s
            i = s
            s = result
            count += 1
        return result
