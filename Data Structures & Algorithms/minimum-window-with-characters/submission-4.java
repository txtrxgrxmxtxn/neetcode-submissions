class Solution{
    public String minWindow(String s, String t){
        if(s.length() < t.length()) return "";
        //required freq. of t.
        int[] need= new int[128];
        for(char c: t.toCharArray()) need[c]++;

        int left = 0, right = 0;
        int required= t.length(); //chars. we have to cover

        int minLen = Integer.MAX_VALUE;
        int minStart = 0;


        while(right < s.length()) {
            char c = s.charAt(right);


            //if this char is still needed, reduce 'required'
            if(need[c] > 0) required --;
            need[c]--; //could be negative

            right ++;
            while (required == 0){
                if (right - left < minLen) {
                    minLen = right - left;
                    minStart = left; 
                }

                char l = s.charAt(left);
                need[l]++; //return the character
                if(need[l] > 0) required++; //don't cover t.
                left ++;

            }
        }  

        return minLen == Integer.MAX_VALUE ? "": s.substring(minStart, minStart + minLen);


    }
}