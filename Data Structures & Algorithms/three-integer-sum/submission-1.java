class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // pick one index i first, then do twosum with hashSet for the rest
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();
        for (int i = 0; i < nums.length - 2; i ++) {
            if (i > 0 && nums[i] == nums[i] - 1){
                continue;
            }

            int target =  0 - nums[i];
            Set<Integer> seen = new HashSet<>();
            for (int j = i + 1; j < nums.length; j ++){
                if (seen.contains(target - nums[j])) {
                    List<Integer> triplet = List.of(nums[i], target - nums[j], nums[j]);
                    res.add(triplet);
                }
                seen.add(nums[j]);
            }

        }

        return new ArrayList<>(res);

    }
}
