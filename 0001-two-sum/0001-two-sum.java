class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> possibleResults = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            
            if (possibleResults.containsKey(nums[i])){
                return new int[]{possibleResults.get(nums[i]), i};
                
            }
            else {
                possibleResults.put(complement, i);
            }
        }
        
        return new int[]{};
    }
}