/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    for (let i = nums.length - k; i < nums.length; i++){
        const changeNumber = nums.pop()
        nums.unshift(changeNumber)
    }

};