function maxProfit(prices: number[]): number {
    if (prices.length === 0){
        return 0
    }
    
    let bestTimeToBuy = prices[0];
    let bestTimeToSell = prices[0];
    let profix = 0
    
    for (const day of prices){
        if (day < bestTimeToBuy){
            bestTimeToBuy = day
            bestTimeToSell = day
        }
        
        else if (day > bestTimeToSell){
            bestTimeToSell = day
            let currentProfix = bestTimeToSell - bestTimeToBuy;
            
            if (currentProfix > profix){
                profix = currentProfix
            }
        }
    }
    
    return profix;
};