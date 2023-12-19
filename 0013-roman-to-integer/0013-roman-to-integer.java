class Solution {
    public int romanToInt(String s) {
        
        Map<Character, Integer> romanNumber = new HashMap<>();
        romanNumber.put('I', 1);
        romanNumber.put('V', 5);
        romanNumber.put('X', 10);
        romanNumber.put('L', 50);
        romanNumber.put('C', 100);
        romanNumber.put('D', 500);
        romanNumber.put('M', 1000);
        
        int total = 0;
        
        for (int i = 0; i < s.length(); i++){
            if ((i < s.length() - 1) && romanNumber.get(s.charAt(i)) < romanNumber.get(s.charAt(i+1))){
                total -= romanNumber.get(s.charAt(i));
            }
            else {
                total += romanNumber.get(s.charAt(i));
            }
        }
        return total;
    }
}