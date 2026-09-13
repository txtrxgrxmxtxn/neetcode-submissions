


class Solution{

    public boolean isHappy(int n){
        Set<Integer> seen = new HashSet<>();

        while(n != 1 && !seen.contains(n)){

            seen.add(n);
            n = sumOfSquares(n);
        }

        return n==1;
    }

    private int sumOfSquares(int n){
        int total = 0;
        while( n > 0){
            int digit = n % 10;
            total += digit * digit; 
            n/= 10;
            
        }

        return total;

    }
}