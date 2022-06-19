var fib = function(n) {
    // Тупо решаю тернарным оператором и рекурсией
    return n <= 1 ? n : fib(n - 1) + fib(n - 2)
};