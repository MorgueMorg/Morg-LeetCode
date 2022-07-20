// Метод доступа size возвращает количество (уникальных) элементов в объекте Set

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  let hasht = {};
  for (let i = 0; i < s.length; i++) {
    if (!hasht["s" + s[i]]) hasht["s" + s[i]] = t[i];
    if (!hasht["t" + t[i]]) hasht["t" + t[i]] = s[i];
    if (t[i] != hasht["s" + s[i]] || s[i] != hasht["t" + t[i]]) return false;
  }
  return true;
};


/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  let arr1 = {};
  let arr2 = {};
  for (let i = 0; i < s.length; i++) {
    if (arr1[s[i]] != arr2[t[i]]) {
      return false;
    } else {
      arr1[s[i]] = i;
      arr2[t[i]] = i;
    }
  }
  return true;
};


/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  let map = new Map();
  if (new Set(s).size != new Set(t).size) return false;
  for (let i = 0; i < s.length; i++) {
    if (map.get(s[i]) && map.get(s[i]) != t[i]) {
      return false;
    } else {
      map.set(s[i], t[i]);
    }
  }
  return true;
};
