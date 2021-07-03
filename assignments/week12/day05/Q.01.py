"""
Q-1 ) Top K Frequent Elements (5 marks)
https://leetcode.com/problems/top-k-frequent-elements/
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        dict = collections.Counter(nums)
        for val, count in dict.items():
            if len(res)<k:
                heapq.heappush(res,(count,val))
            else:
                heapq.heappush(res,(count,val))
                heapq.heappop(res)
        return [val for count, val in res] 