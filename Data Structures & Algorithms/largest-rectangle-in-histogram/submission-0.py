class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # [7, 1, 7, 2, 2, 4] 
        # so each bar is gonna be side by side
        # it's only a rectangle if you can cut out a row of bars of the same height
        # 1. check every subarray and compute max height --> brute force
        # 2. Prefix/postfix --> mininum seen so far at each index? 
        # the last element less than curr 
        # lowkey I can just do binary search 


        #stack

        stack = [(0, -1)]
        res = 0

        for i in range(len(heights)):
            curr_h = heights[i]
            if curr_h >= stack[-1][0]:
                stack.append((curr_h, i))
            else:
                prev_i = i - 1
                while curr_h < stack[-1][0]:
                    prev_h, prev_i = stack.pop()
                    res = max(res, (i - prev_i) * prev_h)
                stack.append((curr_h, prev_i))

        while stack:
            prev_h, prev_i = stack.pop()  
            res = max(res, (len(heights) - prev_i) * prev_h)
        
        return res

        
