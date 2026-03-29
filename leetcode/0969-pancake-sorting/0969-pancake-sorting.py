class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            i = arr.index(size)

            if i == size - 1:
                continue

            if i != 0:
                arr[:i+1] = arr[:i+1][::-1]
                res.append(i + 1)

            arr[:size] = arr[:size][::-1]
            res.append(size)

        return res