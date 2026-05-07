# Last updated: 5/7/2026, 10:26:06 PM
1import heapq
2from collections import defaultdict
3
4class Twitter:
5    def __init__(self):
6        self.count = 0  
7        self.tweet_map = defaultdict(list) 
8        self.follow_map = defaultdict(set)  
9
10    def postTweet(self, userId: int, tweetId: int) -> None:
11        self.tweet_map[userId].append([self.count, tweetId])
12        self.count -= 1
13
14    def getNewsFeed(self, userId: int) -> list[int]:
15        res = []
16        min_heap = []
17
18        self.follow_map[userId].add(userId)
19        
20        for followeeId in self.follow_map[userId]:
21            if followeeId in self.tweet_map:
22                index = len(self.tweet_map[followeeId]) - 1
23                count, tweetId = self.tweet_map[followeeId][index]
24                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
25
26        while min_heap and len(res) < 10:
27            count, tweetId, followeeId, idx = heapq.heappop(min_heap)
28            res.append(tweetId)
29            
30            if idx >= 0:
31                count, tweetId = self.tweet_map[followeeId][idx]
32                heapq.heappush(min_heap, [count, tweetId, followeeId, idx - 1])
33        return res
34
35    def follow(self, followerId: int, followeeId: int) -> None:
36        if followerId != followeeId:
37            self.follow_map[followerId].add(followeeId)
38
39    def unfollow(self, followerId: int, followeeId: int) -> None:
40        if followeeId in self.follow_map[followerId]:
41            self.follow_map[followerId].remove(followeeId)
42
43
44# Your Twitter object will be instantiated and called as such:
45# obj = Twitter()
46# obj.postTweet(userId,tweetId)
47# param_2 = obj.getNewsFeed(userId)
48# obj.follow(followerId,followeeId)
49# obj.unfollow(followerId,followeeId)