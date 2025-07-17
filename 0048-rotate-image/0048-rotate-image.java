class Solution {
    public void rotate(int[][] m) {
        for(int i = 0; i<m.length; i++){
            for(int j = 0; j<m[i].length; j++){
                if(j<=i){
                    int temp = m[i][j];
                    m[i][j] = m[j][i];
                    m[j][i] = temp;
                }
            }
        }
        for(int i = 0; i < m.length; i++){
            int l = 0;
            int r= m[i].length-1;
            while(l<=r){
                int temp = m[i][l];
                m[i][l] = m[i][r];
                m[i][r] = temp;
                l++;
                r--;
            }
        }
    }
}