class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #only consider a number as the starting point in n - 1 does not exist in the array
        nums_set = set(nums)
        print(nums_set)
        count = 0

        for item in nums_set:
            current = 0
            if (item - 1 not in nums_set):
                while(item + current in nums_set):
                    current += 1
            count = max(count, current)
        return count 

            
            





        