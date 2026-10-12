from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque(i for i, party in enumerate(senate) if party == "R")
        dire = deque(i for i, party in enumerate(senate) if party == "D")
        while radiant and dire:
            first, second = radiant.popleft(), dire.popleft()
            if first < second:
                radiant.append(first + len(senate))
            else:
                dire.append(second + len(senate))
        return "Radiant" if radiant else "Dire"
