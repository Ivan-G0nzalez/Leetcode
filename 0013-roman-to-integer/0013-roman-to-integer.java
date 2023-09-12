class Solution {
    public int romanToInt(String s) {
        
        Map<Character, Integer> roman_number = new HashMap<>();
        
        roman_number.put('I', 1);
        roman_number.put('V', 5);
        roman_number.put('X', 10);
        roman_number.put('L', 50);
        roman_number.put('C', 100);
        roman_number.put('D', 500);
        roman_number.put('M', 1000);
        
        int result = 0;
            
        for (int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1 && roman_number.get(s.charAt(i)) < roman_number.get(s.charAt(i+1))) {
                result -= roman_number.get(s.charAt(i));
            } else {
                result += roman_number.get(s.charAt(i));
            }
        }
        
        return result;
    }
}