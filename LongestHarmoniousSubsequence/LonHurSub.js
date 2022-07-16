/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function (nums) {
  let res = 0,
    map = new Map();
  nums.forEach((n) =>
    map.has(n) ? map.set(n, map.get(n) + 1) : map.set(n, 1)
  );
  for (let key of map.keys()) {
    if (map.has(key - 1)) {
      res = Math.max(res, map.get(key) + map.get(key - 1));
    }
  }
  return res;
};
