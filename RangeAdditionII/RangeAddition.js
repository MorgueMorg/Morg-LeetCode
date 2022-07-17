/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} ops
 * @return {number}
 */
var maxCount = function (m, n, ops) {
  let len = ops.length;
  if (len === 0) return m * n;
  let result = [ops[0][0], ops[0][1]];
  for (let i = 1; i < len; i++) {
    result[0] = Math.min(result[0], ops[i][0]);
    result[1] = Math.min(result[1], ops[i][1]);
  }
  return result[0] * result[1];
};
