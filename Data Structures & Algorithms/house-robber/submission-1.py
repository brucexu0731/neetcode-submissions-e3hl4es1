class Solution:
    def rob(self, nums: List[int]) -> int:
        
        i = len(nums) - 1
        imax = {}
        #imax_e = {}

        imax[i] = nums[i]
        #imax_e[i] = [i]

        imax[i - 1] = max(nums[i - 1], nums[i])
        # if imax[i - 1] == nums[i]:
        #     imax_e[i - 1] = [i]
        # else:
        #     imax_e[i - 1] = [i - 1]

        i -= 2
        while i >= 0:
            imax[i] = max(imax[i + 2] + nums[i], imax[i + 1])
            # if imax[i] == nums[i + 1]:
            #     imax_e[i] = imax_e[i + 1]
            # else:
            #     imax_e[i] = [i]
            #     imax_e[i].extend(imax_e[i + 2])
            i -= 1
        
        #print(imax_e[0])
        return imax[0]


        