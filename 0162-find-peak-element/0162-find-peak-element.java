class Solution {
    public int findPeakElement(int[] n) {
        int l = 0;
        int r = n.length-1;
        while(l<=r){
            int m = l+(r-l)/2;
            boolean lg = m>0 && (n[m] < n[m-1]);
            boolean rg = m<n.length-1 && (n[m] < n[m+1]);
            if(lg){
                r = m-1;
            }else if(rg){
                l = m+1;
            }else{
                return m;
            }
        }
        return -1;
    }
}