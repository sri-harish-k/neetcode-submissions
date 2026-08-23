class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = []

        for num in nums:
            if num in seenNums:
                return True
            seenNums.append(num)
        return False