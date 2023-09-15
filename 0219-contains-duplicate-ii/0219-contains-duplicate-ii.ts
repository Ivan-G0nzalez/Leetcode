function containsNearbyDuplicate(nums: number[], k: number): boolean {
  let mapper = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (!mapper.has(nums[i])) {
      mapper.set(nums[i], i);
    } else if (i - mapper.get(nums[i]) <= k) {
      return true;
    } else {
      mapper.set(nums[i], i);
    }
  }
  return false;
};