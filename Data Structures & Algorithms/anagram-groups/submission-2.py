from typing import List
class Solution:

    @staticmethod
    def getDefaultCountMap():
        count_map = {}
        for i in range(ord('a'), ord('z') + 1):
            count_map[chr(i)] = 0

        return count_map

    @staticmethod
    def getChCountMap(string: str) -> dict[str, int]:
        count_map = Solution.getDefaultCountMap()

        for ch in string: 
            count_map[ch] += 1

        return count_map

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        category_map: dict[tuple[tuple[str, int]], List] = {}

        for string in strs:
            ch_count_map = tuple(Solution.getChCountMap(string).items())

            if category_map.get(ch_count_map):
                category_map[ch_count_map].append(string)
            else:
                category_map[ch_count_map] = [string]

        return list(category_map.values())