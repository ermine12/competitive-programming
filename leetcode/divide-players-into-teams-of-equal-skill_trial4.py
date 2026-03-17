class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
 
        sort = sorted(skill)
        l =len(sort)
        target = sort[0] + sort[-1]
        half =l//2
        result = 0
        for i in range(half):
            if sort[i] + sort[l - 1 - i] != target:
                return -1
            result+=sort[i] * sort[l-1-i]

        
        return result

        
             
        