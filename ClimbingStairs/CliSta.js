var climbStairs = function(n) {
    let a = [0,1,2,3]
    for (let i = 4; i <= n; i++) {
        a.push(a[i - 1] + a[i - 2]);
    }

    return a[n];
};