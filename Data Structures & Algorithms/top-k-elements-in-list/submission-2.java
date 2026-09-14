class Solution{ 
    public int[] topKFrequent(int[] nums, int k){
        //Count freq. 
        Map<Integer, Integer> freq = new HashMap<>();
        for(int num : nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        //Create bucket: index = freq, value = list of numbers
        int n = nums.length; 
        List<Integer>[] buckets = new List[n+1];
        for(int i = 0; i<= n; i++){
            buckets[i] = new ArrayList<>();
        }

        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            int num = entry.getKey();
            int f = entry.getValue();
            buckets[f].add(num);
        }


        //iterate buckets from end (major freq.)
        int[] result = new int[k];
        int idx = 0;
        for(int f = n; f >= 0 && idx < k; f-- ){
            for(int num : buckets[f]){
                result[idx++] = num; 
                if ( idx == k) break;
            }
        }

        return result;
    }
}