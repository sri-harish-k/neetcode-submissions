class Solution:
    @staticmethod
    def getTopKFreqElems(map: Dict[int, int], k) -> list[int]:
        count_map = list(map.items())
        n = len(count_map)

        top_k_elems = []

        for i in range(k): # Optimization : sort only until k, we don't need to sort entire array
            for j in range(i+1, n):
                if count_map[j][1] > count_map[i][1]: # compare count
                    temp = count_map[i]
                    count_map[i] = count_map[j]
                    count_map[j] = temp

            top_k_elems.append(count_map[i][0])

        return top_k_elems

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key -> count ; value -> list of num with that count
        num_len = len(nums)
        num_count_map = {}
        top_k_elements = []

        if num_len <= 1 and k <= 1:
            return nums

        # count map
        for num in nums:
            if num in num_count_map:
                num_count_map[num] += 1
            else:
                num_count_map[num] = 1

        return Solution.getTopKFreqElems(num_count_map, k)
        