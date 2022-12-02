class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var result = digits
        var i = digits.count - 1
        result[i] += 1
        while result[i] > 9 {
            if i == 0 {
                result.insert(1, at: 0)
                i += 1
            } else {
                result[i - 1] += 1
            }
            result[i] = 0
            i -= 1
        }
        return result;
    }
}