// Почти такая же логика как на питоне
const isValid = (s) => {
  // Создаю массив куда буду пушить скобки
  const arr = [];
  // Массив со скобками
  const map = new Map([
    ["(", ")"],
    ["[", "]"],
    ["{", "}"],
  ]);
  // Цикл для перебора
  for (let i = 0; i < s.length; i += 1) {
    // Has по сути тоже самое что и includes
    if (map.has(s[i])) {
      // Пушу в массив
      arr.push(map.get(s[i]));
      // Если нет в массиве
    } else if (s[i] !== arr.pop()) {
      return false;
    }
  }

  return arr.length === 0;
};
