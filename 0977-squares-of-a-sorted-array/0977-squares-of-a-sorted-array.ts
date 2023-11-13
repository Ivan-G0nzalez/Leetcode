function sortedSquares(nums: number[]): number[] {
    
    const result = nums.map(num => Math.pow(num, 2))
    result.sort((a,b) => a - b);
    
    return result
};