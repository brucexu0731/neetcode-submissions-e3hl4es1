class Solution {
    public int search(int[] nums, int target) {
        
        int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            if (nums[m] == target) {
                return m;
            }

            if (nums[m] >= nums[0]){
                // sorted left half 
                if (target < nums[m]) {
                    if (target < nums[0]){
                        l = m + 1;
                    } else {
                        r = m - 1;
                    }
                } else {
                    l = m + 1; 
                }
            } else {
                if (target > nums[m]){
                    if (target > nums[nums.length - 1]) {
                        r = m - 1;
                    } else {
                        l = m + 1;
                    }
                } else {
                    r = m - 1;
                }

            }
        }

        return -1;
    }
}
