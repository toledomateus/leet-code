from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapValInd = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapValInd:
                return [mapValInd[diff], i]
            mapValInd[n] = i    
        return