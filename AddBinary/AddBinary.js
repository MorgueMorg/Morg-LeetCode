var addBinary = function (a, b) {
  // Превратил обе строки в массивы, также поменял порядок, потому что будет добавлять с конца
  let result = a.split("").reverse();
  let plus = b.split("").reverse();
  let r = 0;
  // Юзаю цикл для двух массивов
  for (
    let i = 0, j = 0;
    i <= result.length - 1 || j <= plus.length - 1 || r > 0;
    i++, j++
  ) {
    let sum = (parseInt(result[i]) || 0) + (parseInt(plus[j]) || 0) + r;
    if (sum > 1) {
      result[i] = sum % 2;
      r = 1;
    } else {
      result[i] = sum;
      r = 0;
    }
  }
  // Возвращаю обратно перевернутую строку
  return result.reverse().join("");
};
