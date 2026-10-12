from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        blocked = set(deadends)
        if "0000" in blocked:
            return -1
        pending = deque([("0000", 0)])
        seen = {"0000"}
        while pending:
            state, distance = pending.popleft()
            if state == target:
                return distance
            for index in range(4):
                for step in (-1, 1):
                    digit = str((int(state[index]) + step) % 10)
                    following = state[:index] + digit + state[index + 1 :]
                    if following not in blocked and following not in seen:
                        seen.add(following)
                        pending.append((following, distance + 1))
        return -1
