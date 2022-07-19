/**
 * @param {number[][]} img
 * @return {number[][]}
 */
var imageSmoother = function (img) {
  return img.map((arr, i) =>
    arr.map((_, j) => {
      var sum = 0;
      var count = 0;
      for (let l = i - 1; l <= i + 1; l++) {
        for (let m = j - 1; m <= j + 1; m++) {
          if (img[l] && img[l][m] > -1) {
            sum += img[l][m];
            count++;
          }
        }
      }
      return Math.floor(sum / count);
    })
  );
};
