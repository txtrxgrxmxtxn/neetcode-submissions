from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Build adjacency list: adj[pre]: List of courses that depend of 'pre'
        adj = {i: [] for i in range(numCourses)}
        
        #in_degree[crs]: num. of prerequisites 'crs' still needs
        in_degree = [0]*numCourses

        #populate graph in-degrees
        for crs, pre in prerequisites:
            adj[pre].append(crs) #pre must come befor crs
            in_degree[crs] += 1 #crs has one prerequisite


        #queue starts with all courses that must have no prerequisites: 
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        #result: order we build 
        order = []


        #process courses level by level (BFS)
        while queue: 
            crs = queue.popleft() #take a course with all 
            order.append(crs) # add it to the valid order



            #for every course that depends on 'crs' reduce its in-degree 
            for nxt in adj[crs]:
                in_degree[nxt] -= 1

                if in_degree[nxt] == 0:
                    queue.append(nxt)


        return order if len(order) == numCourses else [] 











