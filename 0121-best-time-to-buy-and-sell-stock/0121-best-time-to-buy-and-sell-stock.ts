function maxProfit(prices: number[]): number {
    let betterDayBuy = prices[0];
    let betterDaySell = prices[0];
    
    let maxProfit = 0;
    
    for(let i = 0; i < prices.length; i++){
        if (prices[i] < betterDayBuy){
            betterDayBuy = prices[i];
            betterDaySell = prices[i]
        } else if (prices[i] > betterDaySell){
            betterDaySell = prices[i];
            const currentProfit = betterDaySell - betterDayBuy;
            maxProfit = Math.max(maxProfit, currentProfit)
        }
    }
    
    return maxProfit
};