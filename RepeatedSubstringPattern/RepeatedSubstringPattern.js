/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function (s) {
  return s.repeat(2).slice(1, -1).includes(s);
};


/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function (s) {
  let pattern = "";
  for (let i = 0; i < Math.floor(s.length / 2); i++) {
    pattern += s[i];
    if (pattern.repeat(s.length / pattern.length) === s) return true;
  }
  return false;
};
