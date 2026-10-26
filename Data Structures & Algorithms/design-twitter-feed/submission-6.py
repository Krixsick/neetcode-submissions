import heapq
class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.counter, tweetId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        result = []

        users = self.following.get(userId, set()) | {userId}

        for authorId in users:
            news_feed.extend(self.tweets.get(authorId, []))
        heapq.heapify(news_feed)
        while news_feed and len(result) < 10:
            timestamp, tweetId = heapq.heappop(news_feed)
            result.append(tweetId)
        return result



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
