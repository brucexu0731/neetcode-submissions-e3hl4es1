class Solution {
    public String minWindow(String s, String t) {

        int[] res = {0, 0};
        int resLen = Integer.MAX_VALUE;
        int having = 0;
        Map<Character, Integer> required = new HashMap<>();
        Map<Character, Integer> have = new HashMap<>();

        for (char c : t.toCharArray()){
            required.put(c, required.getOrDefault(c, 0) + 1);
            have.put(c, 0);
        }

        int threshold = required.size();

        int l = 0;
        int r = 0;

        while (r < s.length()) {
            char c = s.charAt(r);
            if(have.containsKey(c)){
                have.put(c, have.get(c) + 1);
                if (have.get(c).equals(required.get(c))){
                    having += 1;
                }
            }

            while(having == threshold) {
                if(r - l + 1 < resLen) {
                    res = new int[]{l, r + 1};
                    resLen = r - l + 1;
                }

                if(have.containsKey(s.charAt(l))){
                    have.put(s.charAt(l), have.get(s.charAt(l)) - 1);
                    if (required.get(s.charAt(l)) > have.get(s.charAt(l))){
                        having -= 1;
                    }
                }

                l ++;
            }

            r++;
        }

        return s.substring(res[0], res[1]);
    }
}
