class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modul = 10 ** 9 + 7
        (a, e, i, o, u) = (1, 1, 1, 1, 1)
        length_permutation = 2
        while length_permutation <= n:
            end_with_a = e + i + u
    
            end_with_e = a + i

            end_with_i = e + o
           
            end_with_o = i
   
            end_with_u = i + o
    
            (a, e, i, o, u) = (end_with_a, end_with_e, end_with_i, end_with_o, end_with_u )
        
            length_permutation += 1
        return (a + e + i + o + u) % modul
            