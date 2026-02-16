class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dictt = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dictt[i+j].append(mat[i][j])
        
        for i in dictt:
            if i%2==0:
                dictt[i].reverse()
        r = list(dictt.values())
        result = [j for i in r for j in i]
        return result




        