/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (words) {
  const rows = [
    new Set("qwertyuiop"),
    new Set("asdfghjkl"),
    new Set("zxcvbnm"),
  ];
  const result = [];
  for (const word of words) {
    const chars = word.toLowerCase().split("");
    for (const row of rows) {
      if (chars.every(row.has, row)) {
        result.push(word);
        break;
      }
    }
  }
  return result;
};


// ! Метод test() проверяет совпадение в строке. Если он находит совпадение, он возвращает true, в противном случае возвращает false. Что то типо инклюда для строк
/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (words) {
  return words.filter(
    (word) =>
      /\b[qwertyuiop]+\b/i.test(word) ||
      /\b[asdfghjkl]+\b/i.test(word) ||
      /\b[zxcvbnm]+\b/i.test(word)
  );
};

