// Метод Math.max() возвращает наибольшее из нуля или более чисел.
var maxSubArray = function(nums) {
    // Переменная для максимального подмассива, 0 потому что идет с начала и массив точно не пустой
    let maxSubArr = nums[0]
    // Цикл для итераций массива
    for (let i = 1; i < nums.length; i++) {
        // Переменная для наибольшего числа из подмассивов с первого и последнего индекса
        nums[i] = Math.max(nums[i], nums[i] + nums[i-1])
        // Максимальный подмассив
        maxSubArr = Math.max(maxSubArr, nums[i]);
    }
    // Возврат по условию
    return maxSubArr
};