class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count number freq. 
        freq_map = {}

        for num in nums: 
            freq_map[num] = freq_map.get(num, 0)+1


        #sort by freq. and obtain mos k frequent. 
        sorted_items = sorted(freq_map.items(), key = lambda x:x[1], reverse = True)

        #extract only numbers

        return [item[0] for item in sorted_items[:k]]