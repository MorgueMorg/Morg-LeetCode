class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {"type": 0, "color": 1, "name": 2}
        count = 0
        for item in items:
            if item[dic[ruleKey]] == ruleValue:
                count += 1
        return count