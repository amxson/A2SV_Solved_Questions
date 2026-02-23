class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill)-1
        z = skill[i]+skill[j]
        x = 0
        while(i<j):
            if(skill[i]+skill[j] == z):
                x += skill[i]*skill[j]
                i +=1
                j -=1
            else:
                return -1
        return x