class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        #if s1 is greater than s2 can't exist a permutation
        if len(s1) > len(s2):
            return False 

        #create counters
        s1_count = [0]*26
        window_count = [0]*26


        #fill content of s1
        for char in s1:
            s1_count[ord(char)-ord('a')]+=1

        #initialize window with first len(s1) chars of s2
        for i in range(len(s1)):
            window_count[ord(s2[i])-ord('a')]+=1


        
        #verify if initial window is a permutation
        if s1_count == window_count: 
            return True


        # Iterate window through all s2
        for i in range(len(s1), len(s2)):
            # add new char to window
            window_count[ord(s2[i])-ord('a')] += 1



            #remove oldest char of window
            window_count[ord(s2[i-len(s1)])-ord('a')] -=1


            #verify if actual window could be a permutation
            if s1_count == window_count:
                return True

        return False 










