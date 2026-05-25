import collections
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = collections.Counter(words)
        heap = [(-freq, word) for word, freq in counts.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]