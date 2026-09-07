class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();
        
        //create the hash string for each word
        for (String word : strs){
            int[] freq = new int[26];
            for (char c : word.toCharArray()) {
                freq[c - 'a'] += 1;
            }

            String key = Arrays.toString(freq);
            anagrams.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        List<List<String>> res = new ArrayList<>();

        for (String key : anagrams.keySet()){
            res.add(anagrams.get(key));
        }

        return res;
    }
}
