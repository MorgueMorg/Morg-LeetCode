class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxtotal = 0
        for i in range(len(accounts)):
            acc = sum(accounts[i])
            maxtotal = max(maxtotal, acc)
        return maxtotal