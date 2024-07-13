class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapValInd = {}
        count = target
        answer: List[int] = []
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapValInd:
                return [mapValInd[diff], i]
            mapValInd[n] = i    
        return