import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Solution {
    public int majorityElement(int[] nums) {
        int size = nums.length / 2; 

        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) { 
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            } else {
                map.put(nums[i], 1);
            }
        }

        int expectedFrequency = Integer.MIN_VALUE;

        for (Entry<Integer, Integer> entry : map.entrySet()) {
            int element = entry.getKey();
            int actualFrequency = entry.getValue();

            if (actualFrequency > size) { 
                return element;
            }
        }

        return -1;
    }
}