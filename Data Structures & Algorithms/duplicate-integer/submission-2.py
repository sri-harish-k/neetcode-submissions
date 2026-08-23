class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can just use set (hashset), since we don't we need to keep track of the count of the nums
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False