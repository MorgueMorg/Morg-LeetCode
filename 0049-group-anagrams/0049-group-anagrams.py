class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for i in strs:
            ele = "".join(sorted(list(i)))
            if ele not in table:
                table[ele] = []
            table[ele].append(i)
        return list(table.values())