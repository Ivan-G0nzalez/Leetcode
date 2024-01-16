class Solution {
    
    private int sumArray(int[] array){
        int total = 0;
        for (int i : array){
            total += i;  // Sum the actual values of the array elements
        }
        return total;
    }
    
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sumGas = sumArray(gas);
        int sumCost = sumArray(cost);
        
        if (sumGas < sumCost){
            return -1;
        }
        
        int total = 0;
        int res = 0;
        
        for (int i = 0; i < gas.length; i++){
            total += gas[i] - cost[i];

            if (total < 0){
                total = 0;
                res = i + 1;
            }
        }
        
        return res;
    }
}
