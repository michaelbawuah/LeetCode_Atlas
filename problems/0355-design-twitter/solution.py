from heapq import heapify, heappop, heappush


class Twitter:
    def __init__(self):
        self._clock = 0
        self._posts = {}
        self._following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._posts.setdefault(userId, []).append((self._clock, tweetId))
        self._clock += 1

    def getNewsFeed(self, userId: int):
        sources = self._following.get(userId, set()) | {userId}
        frontier = []
        for source in sources:
            posts = self._posts.get(source, [])
            if posts:
                index = len(posts) - 1
                time, tweet = posts[index]
                frontier.append((-time, tweet, source, index))
        heapify(frontier)
        result = []
        while frontier and len(result) < 10:
            _, tweet, source, index = heappop(frontier)
            result.append(tweet)
            if index:
                time, previous = self._posts[source][index - 1]
                heappush(frontier, (-time, previous, source, index - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self._following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._following.get(followerId, set()).discard(followeeId)
