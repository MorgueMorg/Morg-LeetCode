/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function (word) {
  if (word === word.toUpperCase()) return true;
  if (word === word.toLowerCase()) return true;
  if (word[0] === word[0].toUpperCase()) {
    let leftOutStr = word.slice(1);
    if (leftOutStr === leftOutStr.toLowerCase()) return true;
  }
  return false;
};


/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function (word) {
  return (
    word === word.toUpperCase() ||
    word === word[0] + word.substr(1).toLowerCase()
  );
};
