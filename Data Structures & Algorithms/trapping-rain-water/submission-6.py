class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        vol = 0
        prev_max = [0, 0]
        prev_vol = 0
        for i in range(1, len(height)):
            if height[i - 1] > height[i]:
                L = i - 1
                prev_max = [height[L], L]
                break
        R = L + 2

        while L < len(height) and R < len(height):
            if height[R] > height[R - 1]:
                if R + 1 == len(height) or height[R + 1] < height[R]:
                    print(L, R)
                    print(prev_max)
                    print(prev_vol)
                    if height[L] >= prev_max[0]:
                        prev_max = [height[L], L]
                        h, l = prev_max
                        vol += min(h, height[R]) * (R - l - 1)
                        for i in range(l + 1, R):
                            vol -= min(height[i], min(h, height[R]))
                    else:
                        h, l = prev_max
                        vol = min(h, height[R]) * (R - l - 1)
                        for i in range(l + 1, R):
                            vol -= min(height[i], min(h, height[R]))
                        vol += prev_vol

                    if height[R] > h:
                        prev_max = [height[R], R]
                        prev_vol = vol

                    L = R
                    R += 2
                else: 
                    R += 1

            else:
                R += 1

        return vol
                
