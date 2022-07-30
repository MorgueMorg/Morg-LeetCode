/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  let ans = 0;
  let obj = {};
  for (let i of s) {
    obj[i] = (obj[i] || 0) + 1;
    if (obj[i] % 2 == 0) ans += 2;
  }
  return s.length > ans ? ans + 1 : ans;
};
