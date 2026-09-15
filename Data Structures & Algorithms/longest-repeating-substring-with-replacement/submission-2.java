class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;
        int r = 0;
        int res = 0;
        int maxMajority = 0;
        Map<Character, Integer> window = new HashMap<>();

        while(r < s.length()) {
            
            window.put(s.charAt(r), window.getOrDefault(s.charAt(r), 0) + 1);
            maxMajority = Math.max(window.get(s.charAt(r)), maxMajority);
            if (r - l + 1 > k + maxMajority){
                window.put(s.charAt(l), window.get(s.charAt(l)) - 1);
                l ++;
            }

            res = Math.max(res, r - l + 1);
            r ++;

        }
        return res;
    }

}
