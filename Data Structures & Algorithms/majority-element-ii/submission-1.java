class Solution {
    public List<Integer> majorityElement(int[] nums) {
        //frequency hashmap
        Map<Integer, Integer> freq = new HashMap<>();
        Set<Integer> res = new HashSet<>();
        int n = nums.length;

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            if (freq.get(num) > n / 3.0){
                res.add(num);
            }
        }

        return new ArrayList<>(res);

    
    }
}