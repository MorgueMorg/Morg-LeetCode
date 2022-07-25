/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  let vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"];
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (vowels.indexOf(s[i]) !== -1) {
      stack.push(s[i]);
    }
  }
  let ans = [];
  for (let i = 0; i < s.length; i++) {
    if (vowels.indexOf(s[i]) !== -1) {
      ans.push(stack.pop());
    } else {
      ans.push(s[i]);
    }
  }
  return ans.join("");
};
