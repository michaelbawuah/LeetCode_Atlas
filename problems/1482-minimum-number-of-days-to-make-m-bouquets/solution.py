class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            day = (left + right) // 2
            run = bouquets = 0
            for bloom in bloomDay:
                run = run + 1 if bloom <= day else 0
                if run == k:
                    bouquets += 1
                    run = 0
            if bouquets >= m:
                right = day
            else:
                left = day + 1
        return left
