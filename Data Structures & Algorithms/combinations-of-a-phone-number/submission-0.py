class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums = list(digits)
        letters_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        def dfs(string, i):
            if i >= len(digits):
                res.append(string)
                return
            
            letters = letters_map[nums[i]]
            for c in letters:
                copy_str = string[:]
                copy_str += c
                dfs(copy_str, i + 1)
            
        dfs('', 0)
        return res