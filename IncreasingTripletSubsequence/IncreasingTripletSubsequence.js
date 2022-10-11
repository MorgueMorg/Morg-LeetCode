/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function (nums) {
  let one = Infinity;
  let two = Infinity;
  for (let i of nums) {
    if (i <= one) {
      one = i;
    } else if (i <= two) {
      two = i;
    } else {
      return true;
    }
  }
  return false;
};
