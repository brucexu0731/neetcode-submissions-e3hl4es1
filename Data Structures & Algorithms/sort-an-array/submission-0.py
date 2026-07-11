class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1, arr2):
            res = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            res += arr1[i:]
            res += arr2[j:]
            return res

        def ms(l, r):
            if l == r:
                return [nums[l]]
            m = (l + r) // 2
            return merge(ms(l, m), ms(m + 1, r))
        
        return ms(0, len(nums) - 1)
