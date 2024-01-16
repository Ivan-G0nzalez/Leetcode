class Solution {
    public String intToRoman(int num) {
        String[][] romans = {
            {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
            {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
            {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
            {"", "M", "MM", "MMM"}
        };
        
        
        int thousands = (int) Math.floor(num / 1000);
        int hundres = (int) Math.floor((num % 1000) / 100);
        int tens = (int) Math.floor((num % 100) / 10);
        int ones = (int) Math.floor(num % 10);
        
        String result = romans[3][thousands] + romans[2][hundres] + romans[1][tens] + romans[0][ones];
        
        return result;
    }
}