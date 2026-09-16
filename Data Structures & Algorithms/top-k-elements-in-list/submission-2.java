class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> min_heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        for (int num : freq.keySet()){
            min_heap.offer(new int[]{freq.get(num), num});
            if (min_heap.size() > k) {
                min_heap.poll();
            }
        }

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = min_heap.poll()[1];
        }

        return res;
    }
}
