class Solution:


    def encode(self, strs: List[str]) -> str:
        #List of encoded string 
        encoded = []


        #Codify each string with format: length#string

        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)

        #join all
        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:

        #list of decodified strings:
        decoded=[]

        #index to iterate decodified string
        index = 0

        while index < len(s):

            #find position of '#'
            j = index
            while s[j] != '#':
                j += 1



            #extract length of string 
            length = int(s[index:j])

            #estimate begin and end of string
            start = j + 1
            end = start + length 
               
            #extract the string + add to result
            decoded.append(s[start:end])

            #move index to next codified string
            index = end
            
        return decoded





