"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #Ordenar por hora de inicio
        intervals.sort(key= lambda x: x.start)


        #verificar solapes
        for i in range(1, len(intervals)):

            #Si el inicio actual es menor que el fin anterior ---> conflicto

            if intervals[i].start < intervals[i-1].end:
                return False


        return True 
