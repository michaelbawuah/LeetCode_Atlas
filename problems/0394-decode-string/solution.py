class Solution:
    def decodeString(self, s: str) -> str:
        stack, pieces, count = [], [], 0
        for letter in s:
            if letter.isdigit():
                count = count * 10 + int(letter)
            elif letter == "[":
                stack.append((pieces, count))
                pieces, count = [], 0
            elif letter == "]":
                expanded = "".join(pieces)
                pieces, repetitions = stack.pop()
                pieces.append(expanded * repetitions)
            else:
                pieces.append(letter)
        return "".join(pieces)
