class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        arr = []
        if len(s) != len(goal): return False
        if s == goal and len(set(s)) < len(s):
            return True
        for i in range(len(s)):
            if s[i] != goal[i]:
                arr.append(i)
        if len(arr)==2 and s[arr[0]]==goal[arr[1]] and s[arr[1]]==goal[arr[0]]:
            return True
        else:
            return False