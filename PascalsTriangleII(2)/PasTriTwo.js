/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  let res = [];
  for (let i = 0; i <= rowIndex; i++) {
    res.unshift(1);
    for (let j = 1; j < i; j++) {
      res[j] += res[j + 1];
    }
  }
  return res;
};
