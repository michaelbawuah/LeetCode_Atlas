from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        distance = {beginWord: 0}
        parents = defaultdict(list)
        pending = deque([beginWord])
        while pending and endWord not in distance:
            for _ in range(len(pending)):
                word = pending.popleft()
                for index in range(len(word)):
                    for letter in "abcdefghijklmnopqrstuvwxyz":
                        if letter == word[index]:
                            continue
                        neighbor = word[:index] + letter + word[index + 1 :]
                        if neighbor not in words:
                            continue
                        if neighbor not in distance:
                            distance[neighbor] = distance[word] + 1
                            pending.append(neighbor)
                        if distance[neighbor] == distance[word] + 1:
                            parents[neighbor].append(word)
        answers = []
        path = [endWord]

        def recover(word):
            if word == beginWord:
                answers.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                recover(parent)
                path.pop()

        if endWord in distance:
            recover(endWord)
        return answers
