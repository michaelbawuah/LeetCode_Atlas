class MyQueue:
    def __init__(self):
        self._incoming = []
        self._outgoing = []

    def push(self, x: int) -> None:
        self._incoming.append(x)

    def _prepare(self):
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())

    def pop(self) -> int:
        self._prepare()
        return self._outgoing.pop()

    def peek(self) -> int:
        self._prepare()
        return self._outgoing[-1]

    def empty(self) -> bool:
        return not self._incoming and not self._outgoing
