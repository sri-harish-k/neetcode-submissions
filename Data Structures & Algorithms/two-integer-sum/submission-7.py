class Solution:
    @staticmethod
    def getNumsPosMap(nums: List[int]) -> dict[int, int]:
        pos_map = {}

        for i, num in enumerate(nums):
            pos_map[num] = i
        
        return pos_map

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_map = Solution.getNumsPosMap(nums)

        for i, num in enumerate(nums):
            # for every i find if there is complement of i (i.e., target - i) and get it's position if exists
            complement = target - num

            complement_pos = pos_map.get(complement, None)
            if complement_pos:
                # we don't want the case where nums[i] + nums[i] = target
                if complement_pos != i:
                    return [i, pos_map[complement]] 

        # control never reaches here
        return [-1, -1]
