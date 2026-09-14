class Solution {
    public int maxArea(int[] heights) {
        
        int l = 0;
        int r = heights.length - 1;
        int res = 0;

        while (l < r) {
            res = Math.max(res, (r - l) * Math.min(heights[r], heights[l]));
            if (heights[r] > heights[l]) {
                l += 1;
            } else {
                r -= 1;
            }
        }

        return res;
    }
}
