class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // calculate the arrival time of each car, then all cars 
        // with the same arrival time would be grouped together 

        // any car can't arrive earlier than its previous car so 
        // it'll take the speed of it's previous car if it's faster
        // take [4,1,0,7], speed = [2,2,1,1]
        // arrival times: [3, 5, 10, 10]
        int[][] sorted = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            int[] ps = {position[i], speed[i]};
            sorted[i] = ps;
        }
        Arrays.sort(sorted, (a, b) -> Integer.compare(a[0], b[0]));

        int count = 0;
        double[] arrivalTimes = new double[position.length];
        for (int i = position.length - 1; i > -1; i--){
            int p = sorted[i][0];
            int s = sorted[i][1];
            //System.out.println(p);
            //System.out.println(s);
            double time = (double)(target - p) / s;
            if (i < position.length - 1 && time <= arrivalTimes[i + 1]){
                arrivalTimes[i] = arrivalTimes[i + 1];
            } else{
                arrivalTimes[i] = time;
                count += 1;
            }
        }
        //System.out.println(Arrays.toString(arrivalTimes));
        return(count);
    }
}
