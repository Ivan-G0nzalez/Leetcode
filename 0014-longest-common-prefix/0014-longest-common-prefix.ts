function longestCommonPrefix(strs: string[]): string {
    
  if (strs.length === 0) return '';

  let ans = '';
  strs.sort();

  let first = strs[0];
  let last = strs[strs.length - 1];

  for (let i = 0; i < Math.min(first.length, last.length); i++) {
    if (first[i] !== last[i]) {
      return ans;
    }
    ans += first[i];
  }

  return ans;
    
};