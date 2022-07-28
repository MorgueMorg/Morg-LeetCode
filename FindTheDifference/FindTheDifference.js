/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
  for (let i of s) t = t.replace(i, "");
  return t;
};


/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
  s = s.split``.sort();
  t = t.split``.sort();
  return t.filter((x, i) => x !== s[i])[0];
};


/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
  let map = {};
  for (const char of t) {
    map[char] ? map[char]++ : (map[char] = 1);
  }
  for (const char of s) {
    map[char]--;
    if (map[char] === 0) delete map[char];
  }
  return Object.keys(map)[0];
};
