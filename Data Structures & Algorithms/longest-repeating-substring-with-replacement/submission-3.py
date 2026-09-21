class Solution: 
    def characterReplacement(self, s: str, k:int) -> int: 
        #counter of char freq. 
        char_count = {}
        left = 0
        max_freq = 0 #most common freq.
        max_length = 0

        #expand window moving right pointer
        for right in range(len(s)):
            # add actual char
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            #update max freq.
            max_freq= max(max_freq, char_count[s[right]])


            #estimate how many chars to replace
            #window_length = right - left + 1 

            #replacements_needed = window_length - max_freq


            # if need + k replacements, reduce window
            while (right-left +1 ) - max_freq > k:
                #remove left char. of window.
                char_count[s[left]] -= 1
                left+=1

            max_length = max(max_length, right-left+1)

        return max_length 
        