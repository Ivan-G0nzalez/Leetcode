function removeDuplicates(nums: number[]): number {
    
    let i = 1;
    let j = 1;
    
    while (i < nums.length){
        if (nums[i - 1] !== nums[i]){
            nums[j] = nums[i];
            j++;
        }
        
        i++;
    }
    
    return j;
};