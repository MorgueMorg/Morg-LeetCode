/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  const map = {};
  for (let letter of magazine) {
    if (!map[letter]) {
      map[letter] = 0;
    }
    map[letter]++;
  }
  for (let letter of ransomNote) {
    if (!map[letter]) {
      return false;
    }
    map[letter]--;
  }
  return true;
};
