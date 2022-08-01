class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = s.replace("-", "").upper()
        each = len(S) % k
        arr = []
        if each:
            arr.append(S[:each])
        for i in range(each, len(S), k):
            arr.append(S[i : i + k])
        return "-".join(arr)


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = s.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+k] for i in range(0, len(S), k))[::-1]