class Solution {
  List<int> plusOne(List<int> digits) {
    for (int i = digits.length - 1; i >= 0; i--){
    if(++digits[i] > 9) digits[i] = 0;
    else return digits;
  }
    digits.insert(0, 1);
    return digits;
  }
}