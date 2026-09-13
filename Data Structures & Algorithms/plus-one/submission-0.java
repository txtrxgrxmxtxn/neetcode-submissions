class Solution {
    public int[] plusOne(int[] digits){
        int n = digits.length;

        // Iterate starting last digit
        for ( int i= n-1; i >= 0; i--){
            // if is less than 9, add 1 and return
            if(digits[i] < 9){
                digits[i] ++; 
                return digits;
            }
            
            //if is 9, convert to 0 and continue
            digits[i] = 0; 
        }

        // If we come here, all numbers are 9
        int[] result = new int[n + 1];
        result[0] = 1;
        return result; 

    }
}