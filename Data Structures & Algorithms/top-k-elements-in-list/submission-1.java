class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> min_heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int num: freq.keySet()){
            int[] pair = {freq.get(num), num};
            min_heap.offer(pair);

            if (min_heap.size() > k) {
                min_heap.poll();
            }
        }

        List<Integer> res = new ArrayList<>();

        while(!min_heap.isEmpty()){
            int[] pair = min_heap.poll();
            res.add(pair[1]);
        }

        return res.stream()
                .mapToInt(Integer::intValue)
                .toArray();

    }
}
