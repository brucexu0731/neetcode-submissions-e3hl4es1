class Solution {

    public String encode(List<String> strs) {
        String res = "";

        for (String str: strs) {
            int len = str.length();
            res += len + "#" + str;
        }

        return res;
    }

    public List<String> decode(String str) {

        System.out.println(str);
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()){
            System.out.println(i);
            int j = i;
            while (str.charAt(j) != '#') {
                j += 1;
            }
            String length = str.substring(i, j);
            int l = Integer.parseInt(length);

            i = j + 1;
            String word = str.substring(i, i + l);
            res.add(word);
            i += l;
        }

        return res;


    }
}
