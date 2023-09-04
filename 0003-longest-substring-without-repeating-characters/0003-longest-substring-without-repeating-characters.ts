function lengthOfLongestSubstring(s: string): number {

    if (s.length === 1){
        return 1
    }

    let result = ""
    let comparation = ""

    for (let letter of s){

        if (comparation.length > result.length){
            result = comparation
        }

        if (!comparation.includes(letter)){
            comparation += letter;
        }
        else{
            comparation = comparation.slice(comparation.indexOf(letter) + 1) + letter;
        }
    }
    
    return Math.max(result.length, comparation.length)
};