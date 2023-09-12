function romanToInt(s: string): number {
    let romanNumber = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    let result = 0;
    
    for (let i = 0; i < s.length; i++){
        if (romanNumber[s[i]] < romanNumber[s[i+1]]){
            result -=  romanNumber[s[i]]
        }
        else{
            result += romanNumber[s[i]]
        }
    }
    
    return result
};