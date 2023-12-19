class Solution {
    public int maxProfit(int[] prices) {
        int bestDayToBuy = prices[0];
        int bestDayToSell = prices[0];
        
        int maxProfix = 0;
        
        for (int i=1; i<prices.length; i++){
            if (prices[i] < bestDayToBuy){
                bestDayToBuy = prices[i];
                bestDayToSell = prices[i];
            }
            else if (prices[i] >  bestDayToBuy){
                bestDayToSell = prices[i];
                int tempProfix = bestDayToSell - bestDayToBuy;
                maxProfix = Math.max(maxProfix, tempProfix);
            }
        }
        
        return maxProfix;
    }
}