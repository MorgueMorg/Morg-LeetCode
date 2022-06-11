// Почти такая же логика как на питоне
const isValid = (s) => {
  const arr = [];
  const map = new Map([
    ["(", ")"],
    ["[", "]"],
    ["{", "}"],
  ]);

  for (let i = 0; i < s.length; i += 1) {
    // Has по сути тоже самое что и includes
    if (map.has(s[i])) {
      arr.push(map.get(s[i]));
    } else if (s[i] !== arr.pop()) {
      return false;
    }
  }

  return arr.length === 0;
};
