/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  for (let i = 0; i < s.length; i++) {
    if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) return i;
  }
  return -1;
};


/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  let map = {};
  for (let char of s) {
    map[char] ? map[char]++ : (map[char] = 1);
  }
  for (let i = 0; i < s.length; i++) {
    if (map[s[i]] === 1) return i;
  }
  return -1;
};


/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  const obj = {};
  const strArr = s.split("");
  for (let el of strArr) {
    obj[el] = (obj[el] || 0) + 1;
  }
  return strArr.findIndex((value) => obj[value] === 1);
};
