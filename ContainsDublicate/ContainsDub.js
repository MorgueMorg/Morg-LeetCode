/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let obj = {};
  for (let i = 0; i < nums.length; i++) {
    // Если число существует в массиве, возвращается true
    if (obj[nums[i]] === undefined) {
      obj[nums[i]] = true;
    } else {
      return true;
    }
  }
  // Вернуть false если дубликатов нет
  return false;
};


/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // Set содержит онли уникальные значения
  let set = new Set();
  let i = 0;
  while (i < nums.length) {
    // Метод  has() возвращает логическое значение, показывающее, существует ли элемент с указанным значением в объекте  Set или нет.
    if (set.has(nums[i])) return true;
    set.add(nums[i]);
    i++;
  }
  return false;
};


/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let set = new Set();
  for (let i = 0; i < nums.length; i++) {
    if (set.has(nums[i])) {
      return true;
    }
    set.add(nums[i]);
  }
  return false;
};
