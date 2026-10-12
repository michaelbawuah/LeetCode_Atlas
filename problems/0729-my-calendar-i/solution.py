class MyCalendar:
    def __init__(self):
        self._bookings = []

    def book(self, start: int, end: int) -> bool:
        if any(start < old_end and old_start < end for old_start, old_end in self._bookings):
            return False
        self._bookings.append((start, end))
        return True
