class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # saw hint 1, 2, 3

        nums_len = len(nums)

        if nums_len <= 0:
            return nums

        prefix = 1
        res = [1] * nums_len

        for i in range(1, nums_len):
            res[i] = nums[i - 1] * prefix
            prefix = res[i]

        prefix = 1
        for i in range(nums_len - 2, -1, -1):
            res[i] = nums[i + 1] * prefix * res[i]
            prefix = nums[i + 1] * prefix

        return res