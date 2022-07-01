/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  for (let i = nums.length; i--; ) {
    if (nums[i] === 0) {
      nums.splice(i, 1) && nums.push(0);
    }
  }
};


/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var moveZeroes = function (nums) {
    let index = 0;
    for(let i=0; i < nums.length; i++){
        if(nums[i] != 0) {
            nums[index] = nums[i];
            index ++;
        }
    }
    for(let j = index; j < nums.length; j++) {
        nums[j] = 0;
    }
};
