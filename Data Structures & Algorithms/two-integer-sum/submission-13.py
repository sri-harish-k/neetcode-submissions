class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # finding the pos map for the entire array is waste of time

        pos_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            complement_pos = pos_map.get(complement, None)
            if complement_pos != None:
                return [complement_pos, i] # using min and max is not necessary as complement_pos is always less than i

            pos_map[num] = i

        ## control never reaches here
        print(pos_map)
        return [-1, -1]

