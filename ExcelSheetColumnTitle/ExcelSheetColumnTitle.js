/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function (columnNumber) {
  let res = "";
  while (columnNumber > 0) {
    let r = columnNumber % 26;
    let d = parseInt(columnNumber / 26);
    if (r == 0) {
      r = 26;
      d -= 1;
    }
    res += String.fromCharCode(64 + r);
    columnNumber = d;
  }
  return res.split("").reverse().join("");
};
