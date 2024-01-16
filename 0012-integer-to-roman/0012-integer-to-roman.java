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
        
        StringBuilder resultBuilder = new StringBuilder();
        resultBuilder.append(romans[3][thousands]);
        resultBuilder.append(romans[2][hundres]);
        resultBuilder.append(romans[1][tens]);
        resultBuilder.append(romans[0][ones]);
        
        String result = resultBuilder.toString();
        
        return result;
    }
}