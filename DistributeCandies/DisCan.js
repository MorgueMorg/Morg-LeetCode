// Метод доступа size возвращает количество (уникальных) элементов в объекте Set

/**
 * @param {number[]} candyType
 * @return {number}
 */
 var distributeCandies = function(candyType) {
    let set = new Set(candyType);
    if (set.size >= candyType.length / 2) return candyType.length / 2;
    else return set.size;
};


/**
 * @param {number[]} candyType
 * @return {number}
 */
 var distributeCandies = function(candyType) {
    return Math.min(candyType.length/2,  new Set(candyType).size)
};