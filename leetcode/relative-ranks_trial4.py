class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score, reverse = True)
        ans = []
        hashs = {}
        for i in sort:
            if sort.index(i) == 0:
                hashs[i]= "Gold Medal"
            elif sort.index(i) == 1:
                hashs[i] = "Silver Medal"
            elif sort.index(i) == 2:
                hashs[i] = "Bronze Medal"
            else:
                hashs[i] = f"{sort.index(i)+1}"
        for j in score:
            ans.append(hashs[j])
        return ans
        

        