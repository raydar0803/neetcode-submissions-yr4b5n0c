class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0 #left pointer 

        for r in range(len(s)): #right pointer r
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l+1
            charSet.add(s[r])
            res = max(res, r - l + 1)    
        return res

        