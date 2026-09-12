class Solution { 
    public boolean exist(char[][] board, String word){
        int rows = board.length;
        int cols = board[0].length;


        // Iterate each cell
        for(int i=0; i < rows; i++){
            for(int j=0; j < cols; j++){
                if(dfs(board, word, i, j, 0)){
                    return true; 
                }
            }
        }

        return false; 
    }

    private boolean dfs(char[][] board, String word, int i, int j, int k){
        if ( k == word.length()){
            //Basic case: complete word  
            return true;
        }

        // check tab limits
        if(i < 0 || i >= board.length || j < 0 || j >= board[0].length){
            return false;
        }
        // Verify that the cell fits with actual character
        if(board[i][j] != word.charAt(k)){
            return false;
        }

        char temp = board[i][j];
        board[i][j] = '#';

        //explore 4 directions
        boolean found = dfs(board, word, i + 1, j, k + 1) || //abajo
                        dfs(board, word, i - 1, j, k + 1) || //arriba
                        dfs(board, word, i, j + 1, k + 1) || // derecha
                        dfs(board, word, i, j - 1, k + 1); //izquierda


        // backtrack
        board[i][j] = temp; 

        return found;

    }
}