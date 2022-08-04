class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D"):
            return True
        return False
        

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'R':[1,0],
            'L':[-1,0],
            'U':[0,1],
            'D':[0,-1]}
        p = [0,0]
        for w in moves:
            m = d[w]
            p[0]+=m[0]
            p[1]+=m[1]
        return p == [0,0]
