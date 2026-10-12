from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        words.add(beginWord)
        width = len(beginWord)
        buckets = defaultdict(list)
        for word in words:
            for index in range(width):
                buckets[word[:index] + "*" + word[index + 1 :]].append(word)
        pending = deque([(beginWord, 1)])
        seen = {beginWord}
        while pending:
            word, length = pending.popleft()
            if word == endWord:
                return length
            for index in range(width):
                key = word[:index] + "*" + word[index + 1 :]
                for neighbor in buckets[key]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        pending.append((neighbor, length + 1))
                buckets[key].clear()
        return 0
