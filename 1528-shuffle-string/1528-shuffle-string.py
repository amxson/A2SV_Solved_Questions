class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [0]*len(s)
        for x, y in zip(s,indices):
            arr[y]=x
        return ''.join(arr)


        