/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
  let pointer1 = 0;
  let pointer2 = s.length - 1;
  while (pointer1 < pointer2) {
    [s[pointer1], s[pointer2]] = [s[pointer2], s[pointer1]];
    pointer1 += 1;
    pointer2 -= 1;
  }
};


/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
 var reverseString = function(s) {
    const helper = (left, right, string) => {
        if (left >= right) return
        [s[left], s[right]] = [s[right], s[left]]
        helper( left+1, right-1, s)
    }
    helper(left = 0, right = s.length - 1, string = s)
};