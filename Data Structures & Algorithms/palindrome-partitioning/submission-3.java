

class Solution{
    public List<List<String>> partition(String s){
        int n = s.length();

        List<List<String>> result = new ArrayList<>();

        boolean[][] isPalindrome = new boolean[n][n];

        for(int i= n-1 ; i >= 0; i --){
            for(int j= i; j< n; j++){
                if(s.charAt(i) == s.charAt(j) && (j-i <= 2 || isPalindrome[i+1][j-1])){
                    isPalindrome[i][j] = true;
                }
            }
        }

        backtrack(s, 0, new ArrayList<>(), result, isPalindrome);
        return result;

    }


    private void backtrack(String s, int start, List<String> current, List<List<String>> result, boolean[][] isPalindrome){
        //Basic case: we reach string end
        if(start == s.length()){

            result.add(new ArrayList<>(current));
            return;
        }

        for (int end = start; end < s.length(); end++ ){
            if (isPalindrome[start][end]){
                current.add(s.substring(start, end+1));
                
                //explore
                backtrack(s, end+1, current, result, isPalindrome);

                //backtrack
                current.remove(current.size() - 1);
            }
        }
    }
}