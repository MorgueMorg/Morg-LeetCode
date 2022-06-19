// ! Брутфорс, полное прохождение не бро
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
};

// ! Хэш-таблица бро
var twoSum = function (nums, target) {
  const indices = new Map();

  for (let index = 0; index < nums.length; index++) {
    const complement = target - nums[index];

    if (indices.has(complement)) {
      return [indices.get(complement), index];
    }

    indices.set(nums[index], index);
  }
};
