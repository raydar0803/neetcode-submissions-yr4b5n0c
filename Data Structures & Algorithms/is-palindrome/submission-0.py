class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        clean_str = "".join(filtered_chars)
        l = 0
        r = len(clean_str) - 1

        while(l<r):
            if(clean_str[l] != clean_str[r]):
                return False
            l += 1
            r -= 1
        return True
        