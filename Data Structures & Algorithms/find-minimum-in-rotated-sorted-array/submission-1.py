class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]
        while(l <= r) :
            mid = (l+r)//2
            if nums[l] <= nums[r]:
                minimum = min(minimum, nums[l])
                break
            minimum = min(minimum, nums[mid])
            if(nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid - 1
        return minimum
