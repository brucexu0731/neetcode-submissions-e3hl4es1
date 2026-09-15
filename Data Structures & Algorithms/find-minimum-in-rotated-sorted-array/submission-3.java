class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        if (nums[0] < nums[nums.length - 1]){
            return nums[0];
        }

        while (l < r) {
            int m = (l + r) / 2;
            if (m > 0 && nums[m] < nums[m - 1]){
                return nums[m];
            }
            //m is currently in the left sorted half 
            if (nums[m] >= nums[0]){
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return nums[l];
    }
}
