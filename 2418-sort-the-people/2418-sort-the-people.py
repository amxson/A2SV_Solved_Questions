class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        
        for i in range(1, n):
            height = heights[i]
            name = names[i]
            j = i - 1
            while j >= 0 and heights[j] < height:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            heights[j + 1] = height
            names[j + 1] = name
        
        return names
