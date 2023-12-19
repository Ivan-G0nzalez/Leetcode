import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Solution {
    public int majorityElement(int[] nums) {
        int num = nums[0];
        int counter = 1;
        
        for (int i = 1; i < nums.length; i++){
            if (num != nums[i]){
                counter--;
            }
            
            else {
                counter++;   
            }
            
            if (counter == 0){
                num = nums[i];
                counter = 1;
            }
            
            
        }
        
        return num;
    }
}