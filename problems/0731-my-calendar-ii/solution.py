class MyCalendarTwo:
    def __init__(self):
        self._bookings = []
        self._doubles = []

    def book(self, start: int, end: int) -> bool:
        if any(start < old_end and old_start < end for old_start, old_end in self._doubles):
            return False
        for old_start, old_end in self._bookings:
            if start < old_end and old_start < end:
                self._doubles.append((max(start, old_start), min(end, old_end)))
        self._bookings.append((start, end))
        return True
