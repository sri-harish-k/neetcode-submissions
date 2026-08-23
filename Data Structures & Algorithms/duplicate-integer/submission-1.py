class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}

        for num in nums:
            if nums_map.get(num, None):
                return True
            else:
                nums_map[num] = 1
        return False