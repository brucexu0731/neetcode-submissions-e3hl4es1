class Solution {
    public int getSum(int a, int b) {
        while ((a & b) != 0) {
            int nxtA = a ^ b;
            b = (a & b) << 1;
            a = nxtA;
        }
        return a ^ b;
    }
}
