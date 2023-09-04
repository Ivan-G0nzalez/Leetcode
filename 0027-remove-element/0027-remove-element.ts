function removeElement(nums: number[], val: number): number {
    let lenArray = 0 ;
    nums.forEach((num, index, array)=>{
        if (num !== val) {
            array[lenArray] = num;
            lenArray++
        }
    })
    
    return lenArray;
};