class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dictionary to store most recent index to each char. 
        char_index = {}
        max_length = 0
        left = 0 #left pointer


        for right in range(len(s)):
            #if char not in the window, move pointer
            if s[right] in char_index and char_index[s[right]] >=left: 
                left = char_index[s[right]] + 1


            #update chars index

            char_index[s[right]] = right


            #update max length:
            max_length = max(max_length, right-left+1)


        return max_length