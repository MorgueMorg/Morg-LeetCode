var searchInsert = function(nums, target) {
    // Перебираю массив в поисках таргета
    for (let i = 0; i < nums.length; i++) {
        // Если нахожу, вовращаю индекс 
        if (nums[i] >= target) {
            return i;
        }
    }
    return nums.length;
};

// ! Бинарный поиск
var searchInsert = function (nums, target) {
    let left = 0;
    let right = nums.length;

    while (left < right) {
        const middle = Math.floor((left + right) / 2);

        if (nums[middle] < target) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }

    return left;
};