class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        L, R = 0, len(height) - 1
        max_left = height[L]
        max_right = height[R]
        tot = 0

        while L <= R:
            if max_left <= max_right:
                tot += max(0, max_left - height[L])
                max_left = max(height[L], max_left)
                L += 1
            else:
                tot += max(0, max_right - height[R])
                max_right = max(height[R], max_right)
                R -= 1
        
        return tot

                
