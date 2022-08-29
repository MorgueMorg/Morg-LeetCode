class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # re-sub -> Возвращает новую строку, полученную в результате замены по указанному шаблону.
        paragraph=re.sub(r'[,.!?;\']',' ',paragraph)
        paragraph=paragraph.lower()
        a=paragraph.split()
        count=0
        word=""
        for i in list(set(a)):
            if a.count(i)>count and i not in banned:
                count=a.count(i)
                word=i
        return word