var removeDuplicates = function(nums) {
    // Cоздаю переменную для сравнения
    let i = 0
    // Создаю цикл и новую вторую переменную для сравнения элементов в массиве
    for (let j = 1; j < nums.length; j++) {
        // Если элементы не равны, то передвигаю первый вперед по итерации
        if (nums[j] !== nums[i]) {
            i+=1
            // Ставлю их вместе
            nums[i] = nums[j]
        } 
    } 
    return i + 1
};