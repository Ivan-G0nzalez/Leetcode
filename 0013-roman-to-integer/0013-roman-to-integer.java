class Solution {
    private int translate(Character character){
        switch(character){
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
        }
        return 0;
    }
    
    public int romanToInt(String s) {
        
        
        int total = 0;
        
        for (int i = 0; i < s.length(); i++){
            if ((i < s.length() - 1) && translate(s.charAt(i)) < translate(s.charAt(i+1))){
                total -= translate(s.charAt(i));
            }
            else {
                total += translate(s.charAt(i));
            }
        }
        return total;
    }
}