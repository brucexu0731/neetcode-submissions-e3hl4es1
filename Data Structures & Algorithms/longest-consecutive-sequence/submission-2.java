class Solution {
    public int longestConsecutive(int[] nums) {
        List<Integer> starts = new ArrayList<>();
        Set<Integer> numSet = new HashSet<>();
        for(int num : nums) {
            numSet.add(num);
        }

        for(int num : nums) {
            if(!numSet.contains(num - 1)) {
                starts.add(num);
            }
        }
        int res = 0;
        for (int num : starts) {
            int count = 0;
            while (numSet.contains(num)){
                num += 1;
                count += 1;
            }
            res = Math.max(res, count);
        }

        return res;

    }
}
