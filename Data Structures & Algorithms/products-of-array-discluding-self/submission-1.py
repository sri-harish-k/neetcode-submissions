class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # saw hint 1, 2, 3

        nums_len = len(nums)

        if nums_len <= 0:
            return nums

        left_prefix = [1] * nums_len
        for i in range(1, nums_len):
            left_prefix[i] = left_prefix[i - 1] * nums[i - 1]

        right_prefix = [1] * nums_len
        for i in range(nums_len - 2, -1, -1):
            right_prefix[i] = right_prefix[i + 1] * nums[i + 1]

        product_except_self = []

        for i in range(nums_len):
            product_except_self.append(left_prefix[i] * right_prefix[i])

        return product_except_self