class TimeMap: 
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int)-> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))



    def get(self, key: str, timestamp: int)-> str:

        if key not in self.data:
            return ""

        list= self.data[key]
        left = 0
        right = len(list) - 1
        result = -1

        #Binary search
        while left <= right: 
            mid = (right + left)// 2

            if list[mid][0] <= timestamp:
                result = mid
                left = mid + 1

            else: 
                right = mid - 1 


        if result == -1:
            return ""


        return list[result][1]

            












        
