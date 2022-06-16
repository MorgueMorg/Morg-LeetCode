var lengthOfLastWord = function(s) {
    // Переменная для последнего слова, trim - убирает пробелы с обоих концов, split разделяет строку по пробелу и возвращает массив из слов которые были в строке 
    let word = s.trim().split(" ");
    // Если длина слова равна нулю, возвратить 0
    if (word.length === 0) {
      return 0;
    } else {
        // Возвращаю длину последнего элемента в массиве, то есть длину последней строки
      return word[word.length - 1].length;
    }
};

var lengthOfLastWord = function(s) {
    // Тоже самое что сверху, только в тернарном операторе
    let word = s.trim().split(" ");
    return word.length > 0 ? word[word.length - 1].length : 0;
};