/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);
  let count = 0,
    i = 0,
    j = 0;
  while (i < s.length && j < g.length) {
    if (s[i] >= g[j]) {
      count += 1;
      i += 1;
      j += 1;
    } else {
      i += 1;
    }
  }
  return count;
};


/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);
  let i = 0;
  for (let j = 0; j < s.length; j++) {
    if (i < g.length && g[i] <= s[j]) {
      i += 1;
    }
  }
  return i;
};
