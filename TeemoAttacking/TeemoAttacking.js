/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function (timeSeries, duration) {
  let bro = 0;
  for (i = 0; i < timeSeries.length - 1; i++) {
    bro += Math.min(timeSeries[i + 1] - timeSeries[i], duration);
  }
  return bro + duration;
};
