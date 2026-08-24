class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # gn : solution definitely exists for every input
        # brute force : find i, j exists such that nums[i] + nums[j] = target
        nums_length = len(nums)
        for i in range(nums_length):
            for j in range(i + 1, nums_length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # control flow never reaches here
        return [-1, -1]