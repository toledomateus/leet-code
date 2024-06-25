

# First Solution: T= O(n),S = O(n)
class FirstSolution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0,0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res

# Second Solution: T = O(n), S = O(1)
class SecondSolution:
    # Algorithm Boyer-Moore
    def majorityElement(self, nums: List[int]) -> int: 
        res, count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
