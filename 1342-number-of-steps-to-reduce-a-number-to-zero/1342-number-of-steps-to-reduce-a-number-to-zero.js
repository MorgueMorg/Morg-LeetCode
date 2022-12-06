/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let counter = 0
    while (num > 0) {
        if (num % 2 == 0) {
            num /= 2
            counter += 1
        } else {
            num--
            counter += 1
        }
    }
    return counter
}; 