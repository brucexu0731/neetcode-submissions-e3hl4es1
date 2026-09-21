class Solution {

    List<List<Integer>> res = new ArrayList<>();
    Deque<Integer> path = new ArrayDeque<>();
    int target;
    int[] nums;

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        this.target = target;
        this.nums = nums;

        dfs(0, 0);
        return res;
    }

    void dfs(int i, int sum){
        if(i >= nums.length || sum > target){
            return;
        }
        if (sum == target){
            res.add(new ArrayList<>(path));
            return;
        }

        // two options, skip or add curr 
        dfs(i + 1, sum);

        sum += nums[i];
        path.offerLast(nums[i]);
        dfs(i, sum);
        //backtrack
        sum -= nums[i];
        path.pollLast();

    }


}
