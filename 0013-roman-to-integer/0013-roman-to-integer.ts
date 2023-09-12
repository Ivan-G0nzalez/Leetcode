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
    
    let counter = 0;
    
    for (const number of s){
        counter += romanNumber[number]
    }
    
    
    let restNumber = {
        IV: -2,
        IX: -2,
        XL: -20,
        XC: -20,
        CD: -200,
        CM: -200,
    };

    for (let i = 0; i < s.length; i++) {
        let pair = s[i] + s[i + 1];
        if (restNumber[pair]) {
            counter += restNumber[pair];
            i++;
        }
      }
    
    return counter
    
};