import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for n in range(len(nums)):
            frequency_map[nums[n]] = frequency_map.get(nums[n], 0) + 1
        
        heap = []
        res = []
        for num, freq in frequency_map.items():
            heapq.heappush(heap, (freq, num))
            if(len(heap) > k):
                heapq.heappop(heap)
        return [num for freq, num in heap]

        
        