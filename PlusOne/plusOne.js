var plusOne = function(digits) {
    // Прохожусь циклом по массиву
    for (let i = digits.length - 1; i >= 0; i--) {
        // Условие, если число в массиве больше 9, ++ - играет роль обычного инкремента(+1)
        if (++digits[i] > 9) {
            // То по условию, делаю число нулем
            digits[i] = 0
        } else {
            // Либо возвращаю массив
            return digits
        }
    }
    // По условию приходится добавлять в начало массива 1, чтобы при инпуте с цифрой 9 вышел такой массив: [1, 0]
    digits.unshift(1);
    // Возвращаю сам массив
    return digits;
};

// ! Тупо синтакс сахар без скобок, тоже самое что сверху
// var plusOne = function(digits) {
//     for(let i = digits.length - 1; i >= 0; i--){
//     if(++digits[i] > 9) digits[i] = 0;
//     else return digits;
//   }
//     digits.unshift(1)
//     return digits
// };