class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_str = min(strs, key=len)
        for i,x in enumerate(short_str):
            for other_str in strs:
                if other_str[i] != x:
                    return short_str[:i]
        return short_str
