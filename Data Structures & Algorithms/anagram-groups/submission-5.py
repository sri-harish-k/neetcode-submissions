class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from typing import List
from collections import defaultdict
class Solution:
    @staticmethod
    def getChCountMap(string: str) -> List[int]:
        count_arr = [0] * 26 # index 0 -> count of a, index 1 -> count of b, ...index 25 - count of z

        for ch in string:
            key = ord(ch) - ord('a')
            count_arr[key] += 1

        return count_arr

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is the pattern (like 1 e, 1a, 1t) and value is the string that satisifies it (anagram)
        category_map: dict[tuple, List] = {}

        for string in strs:
            ch_count_map = tuple(Solution.getChCountMap(string))

            if category_map.get(ch_count_map):
                category_map[ch_count_map].append(string)
            else:
                category_map[ch_count_map] = [string]
        return list(category_map.values())