function wordPattern(pattern: string, s: string): boolean {
  let words = s.split(' ');
  let mapper1 = new Map();
  let mapper2 = new Map();
    
    if (words.length !== pattern.length) return false

  for (let i = 0; i < pattern.length; i++) {
    const char = pattern[i];
    const word = words[i];

    if (!mapper1.has(char) && !mapper2.has(word)) {
      mapper1.set(char, word);
      mapper2.set(word, char);
    } else if (mapper1.get(char) !== word || mapper2.get(word) !== char) {
      return false;
    }
  }

  return true;
}