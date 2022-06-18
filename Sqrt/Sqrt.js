var mySqrt = function(x) {
    let left = 0
    let right = x
    if(x < 2) return x;
    while (left < right) {
        let mid = Math.floor((left + right) / 2)
        if (mid * mid > x)  right = mid
        else if (mid * mid < x) left = mid + 1
         else return mid
    }
    return left - 1
}; 