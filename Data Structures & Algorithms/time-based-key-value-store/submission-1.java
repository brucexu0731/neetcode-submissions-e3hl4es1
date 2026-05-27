class Pair {
    String val;
    int time;

    public Pair(String val, int time) {
        this.val = val;
        this.time = time;
    }
}

class TimeMap {

    Map<String, ArrayList<Pair>> map;

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!map.containsKey(key)){
            ArrayList<Pair> values = new ArrayList<>();
            values.add(new Pair(value, timestamp));
            map.put(key, values);
        } else{
            ArrayList<Pair> values = map.get(key);
            values.add(new Pair(value, timestamp));
        }
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)){
            return("");
        }
        ArrayList<Pair> values = map.get(key);
        int l = 0;
        int r = values.size() - 1;
        while(l <= r){
            int m = (l + r) / 2;
            Pair curr = values.get(m);
            if (curr.time == timestamp){
                return curr.val;
            } else if (curr.time < timestamp){
                l = m + 1;
            } else{
                r = m - 1;
            }
        }
        return r == -1 ? "" : values.get(r).val ;
    }
}
