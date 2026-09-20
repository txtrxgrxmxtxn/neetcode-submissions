class Solution:
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = {}

        for word in strs: 
            #create counting array for each word
            count = [0]*26



            #count frequencies of each word
            for char in word: 
                count[ord(char)- ord('a')] +=1


            #convert to tuple to use it as key of hashmap
            key = tuple(count)

            # add word to group
            if key not in anagram_groups:
                anagram_groups[key] = []

            anagram_groups[key].append(word)


        #return the groups formed
        return list(anagram_groups.values())