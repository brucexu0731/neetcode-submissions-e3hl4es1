class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

    #     a b a c 
    #   0 1 2 3 4
    # c 1 2 3 4 4 
    # a 2 2 3 4 5  
    # b 3 3 3 4 5  
        
        rows = len(str2) + 1
        cols = len(str1) + 1

        dp = [0] * cols

        for i in range(1, cols):
            dp[i] = [i, str1[:i]]
        dp[0] = [0, '']

        for i in range(1, rows):
            new_dp = [0] * cols
            new_dp[0] = [i, str2[:i]]
            for j in range(1, cols):
                #print(i, j)
                c1 = str1[j - 1]
                c2 = str2[i - 1]
                if c1 == c2:
                    l, s = dp[j - 1]
                    new_dp[j] = [l + 1, s + c1]
                else:
                    l1, s1 = dp[j]
                    l2, s2 = new_dp[j - 1]
                    if l1 <= l2:
                        new_dp[j] = [l1 + 1, s1 + c2]
                    else:
                        new_dp[j] = [l2 + 1, s2 + c1]
            dp = new_dp
        
        return dp[cols - 1][1]
        

            