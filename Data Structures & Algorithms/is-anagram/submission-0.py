class Solution:
    @staticmethod
    def getLetterCount(string) -> Dict[str, int]:
        letterCount = {}
        for ch in string:
            letterCount[ch] = letterCount.get(ch, 0) + 1
        return letterCount

    def isAnagram(self, s: str, t: str) -> bool:
        # brute force - compare count of letters of each word
        s_LetterCount = Solution.getLetterCount(s)
        t_LetterCount = Solution.getLetterCount(t)

        if len(s_LetterCount) != len(t_LetterCount):
            return False
        
        for i, key in enumerate(s_LetterCount):
            if s_LetterCount[key] != t_LetterCount.get(key, 0):
                return False
        return True
            
