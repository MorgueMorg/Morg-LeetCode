// ! Решение №1 для числа
var isPalindrome = function (x) {
  let s = "" + x;
  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    if (s[l] !== s[r]) return false;
    l++;
    r--;
  }
  return true;
};


// ! Решение №2 для числа
var isPalindrome = function (x) {
  if (x < 0) return false;
  let num = x;
  let res = 0;
  while (num !== 0) {
    res = res * 10 + (num % 10);
    num = Math.floor(num / 10);
  }
  return res === x;
};


// ! Палиндром для строки
const isPalindrome = (str) => { 
    let a = str.split("").reverse().join("")
    if (a === str) {
        return true
    } else {
        return false
    }
}
console.log(isPalindrome("lol"))