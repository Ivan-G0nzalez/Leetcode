import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Solution {
    public int majorityElement(int[] nums) {
        
        int candidate = 0;
        int count = 0;

        // Iterate through the array
        for (int num : nums) {
            // If count is 0, set the candidate to num
            if (count == 0) {
                candidate = num;
            }

     
            count += (candidate == num) ? 1 : -1;
        }

        return candidate;
    }
}