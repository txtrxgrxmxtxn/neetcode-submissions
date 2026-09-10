from typing import List
import heapq 
from collections import defaultdict 

class Twitter: 
    def __init__(self): 
        #Contador global de tiempo ordenar tweets.
        self.timestamp = 0
        #tweets[userId] = [(timestamp, tweetId), ...]
        self.tweets = defaultdict(list)
        #following[userId] = set(followIds)
        self.following = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None: 
        self.timestamp += 1 
        #Añadir tweet a inicio (mas reciente primero)
        self.tweets[userId].append((self.timestamp, tweetId))



    def getNewsFeed(self, userId: int) -> List[int]:
        #Usuarios a consultar: el propio usuario + quienes sigue
        users = self.following[userId] | {userId}


        #max-heap: (-timestamp, tweetId, userId, index)
        heap= []


        for user in users: 
            if self.tweets[user]: 
                #obtener tweet + reciente cada usuario
                idx = len(self.tweets[user]) - 1
                timestamp, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (-timestamp, tweetId, user, idx - 1))



        result= []

        #extraer 10 tweets max.
        while heap and len(result) < 10: 
            neg_timestamp, tweetId, user, next_idx = heapq.heappop(heap)
            result.append(tweetId)




            #Si hay más tweets de este usuario, agregar el siguiente
            if next_idx >= 0: 
                timestamp, next_tweetId = self.tweets[user][next_idx]
                heapq.heappush(heap, (-timestamp, next_tweetId, user, next_idx - 1))

        return result



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

















        
