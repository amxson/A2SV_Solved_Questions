class FrequencyTracker:

    def __init__(self):
        self.num = {}
        self.freq = {}

    def add(self, number: int) -> None:
        old = self.num.get(number, 0)
        self.num[number] = old + 1
        new = old + 1

        if old > 0:
            self.freq[old] = self.freq.get(old, 0) - 1

        self.freq[new] = self.freq.get(new, 0) + 1

    def deleteOne(self, number: int) -> None:
        old = self.num.get(number, 0)
        if old == 0:
            return

        new = old - 1
        self.num[number] = new

        if old > 0 and self.freq.get(old, 0) > 0:
           self.freq[old] -= 1


        if new > 0:
            self.freq[new] = self.freq.get(new, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0
