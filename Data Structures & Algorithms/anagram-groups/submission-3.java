class Solution {
    public List <List <String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();


        for (String s: strs){
            // Count freq. of each lowercase letter
            int[] count = new int[26];
            for(char c: s.toCharArray()) {
                count[c - 'a'] ++;
            }

            // Build unique key from freq. array:
            StringBuilder sb = new StringBuilder();
            for (int freq: count) { 
                sb.append(freq).append('#');

            }

            String key = sb.toString();

            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);




        }
        return new ArrayList<>(map.values());
    }
}