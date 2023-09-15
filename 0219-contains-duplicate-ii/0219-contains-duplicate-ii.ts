function containsNearbyDuplicate(nums: number[], k: number): boolean {
  let mapper = new Map();

    
  for (let i = 0; i< nums.length; i++){
      const currentValue = nums[i]
      if (mapper.has(currentValue) && i - mapper.get(currentValue) <= k){
          return true
      }
      else{
          mapper.set(currentValue, i)
      }
  }
    return false;
}