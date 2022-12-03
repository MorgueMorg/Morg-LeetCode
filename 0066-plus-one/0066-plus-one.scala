object Solution {
    def plusOne(digits: Array[Int]): Array[Int] = {
        for (i <- digits.length - 1 to 0 by -1) {
          if (digits(i) < 9) {
            digits(i) += 1
            return digits
          }
          digits(i) = 0
        }
        1 +: digits
    }
}