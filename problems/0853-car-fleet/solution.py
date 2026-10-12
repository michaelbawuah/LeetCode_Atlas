from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        front_distance = 0
        front_speed = 1
        for start, velocity in sorted(zip(position, speed, strict=True), reverse=True):
            distance = target - start
            if fleets == 0 or distance * front_speed > front_distance * velocity:
                fleets += 1
                front_distance = distance
                front_speed = velocity
        return fleets
