class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p == q:
            return 1
        height = q
        right, up = False, True
        while True:
            if height + q == p:
                if right and up:
                    return 1
                elif not right and up:
                    return 2
                else:
                    return 0
            elif height + q < p:          
                height += q
                right = not right
            else:                           
                height +=  q - p
                right = not right
                up = not up


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p, q = p / 2, q / 2
        return int(1 - p % 2 + q % 2)
