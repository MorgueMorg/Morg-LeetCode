class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        answer = []
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        mid = (sumBob - sumAlice) // 2
        sumSetAlice = set(aliceSizes)
        for bob in bobSizes:
            if bob - mid in sumSetAlice:
                answer.append(int(bob - mid))
                answer.append(bob)
                return answer
        return answer