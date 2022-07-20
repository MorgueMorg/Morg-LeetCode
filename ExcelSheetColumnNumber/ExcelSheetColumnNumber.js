// Метод charCodeAt() возвращает числовое значение Юникода для символа по указанному индексу

/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function (columnTitle) {
  let res = 0;
  for (let i = 0; i < columnTitle.length; i++) {
    res = res * 26 + columnTitle.charCodeAt(i) - "A".charCodeAt(0) + 1;
  }
  return res;
};
