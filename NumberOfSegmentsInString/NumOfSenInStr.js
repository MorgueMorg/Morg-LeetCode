/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function (s) {
  return s.split(" ").filter((x) => x !== "").length;
};


/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function (s) {
  let a = s.split(" ");
  let count = 0;
  for (i = 0; i < a.length; i++) {
    if (a[i] != "") {
      count++;
    }
  }
  return count;
};
