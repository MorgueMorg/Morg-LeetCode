/**
 * @param {number[]} score
 * @return {string[]}
 */
var findRelativeRanks = function (score) {
  let ranks = score.slice(0).sort((a, b) => b - a);
  return score.map((num, i) => {
    if (num === ranks[0]) return "Gold Medal";
    else if (num === ranks[1]) return "Silver Medal";
    else if (num === ranks[2]) return "Bronze Medal";
    else return (ranks.indexOf(num) + 1).toString();
  });
};
