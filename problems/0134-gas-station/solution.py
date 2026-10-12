class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = running = 0
        start = 0
        for index, (fuel, expense) in enumerate(zip(gas, cost, strict=True)):
            difference = fuel - expense
            total += difference
            running += difference
            if running < 0:
                start = index + 1
                running = 0
        return start if total >= 0 else -1
