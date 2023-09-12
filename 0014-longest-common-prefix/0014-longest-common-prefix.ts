function longestCommonPrefix(strs: string[]): string {
    
    strs.sort((strs1, strs2) => strs1.length - strs2.length);
      let firstWord = strs[0];
      let longerPrefix = '';

      for (let i = 0; i < firstWord.length; i++) {
        for (let j = 1; j < strs.length; j++) {
          if (firstWord[i] !== strs[j][i]) {
            return longerPrefix;
          }
        }
        longerPrefix += firstWord[i];
      }

      return longerPrefix;
};