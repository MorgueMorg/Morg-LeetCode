/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function (list1, list2) {
  const map = new Map();
  let ret = [];
  let min = Infinity;
  for (let i = 0; i < list1.length; ++i) {
    map.set(list1[i], i);
  }
  for (let i = 0; i < list2.length; ++i) {
    if (map.has(list2[i])) {
      let index1 = map.get(list2[i]);
      let index2 = i;
      ret.push({ val: list2[i], index: index1 + index2 });
      min = Math.min(min, index1 + index2);
    }
  }
  return ret.filter((item) => item.index === min).map((item) => item.val);
};
