function isSubsequence(s: string, t: string): boolean {
    let start_s = 0;
    let start_t = 0;
    
    if (s.length == 0){
        return true
    }
    
    while (start_t < t.length){
        if (s[start_s] === t[start_t]){
            start_s++;
        }
        
        if (start_s === s.length){
            return true
        }
        
        start_t++;
    }
    
    return false;
};