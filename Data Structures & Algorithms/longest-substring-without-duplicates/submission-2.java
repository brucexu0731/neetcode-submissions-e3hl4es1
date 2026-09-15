class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int r = 0;
        int res = 0;

        Set<String> window = new HashSet<>();
        while(r < s.length()){

            while(window.contains(s.substring(r, r + 1))){
                window.remove(s.substring(l, l + 1));
                l += 1;
            }
            res = Math.max(res, r - l + 1);
            window.add(s.substring(r, r + 1));
            r += 1;
        }

        return res;
    }
}
