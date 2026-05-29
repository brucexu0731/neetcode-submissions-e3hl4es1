from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.posts = defaultdict(list)
        self.tweet_time = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # larger tweetID means more recent 
        self.followings[userId].add(userId)
        self.posts[userId].append(tweetId)
        self.tweet_time[tweetId] = self.timestamp
        self.timestamp += 1
        print(self.followings)
        print(self.posts)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for user in self.followings[userId]:
            for post in self.posts[user]:
                time = self.tweet_time[post]
                if len(tweets) < 10:
                    heapq.heappush(tweets, (time, post))
                else:
                    if time > tweets[0][0]:
                        heapq.heappop(tweets)
                        heapq.heappush(tweets, (time, post))
        
        res = [0] * len(tweets)
        for i in range(len(tweets) - 1, -1, -1):
            res[i] = heapq.heappop(tweets)[1]
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.followings[followerId]:
            return
        self.followings[followerId].remove(followeeId)
