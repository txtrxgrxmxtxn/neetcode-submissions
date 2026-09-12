class PrefixTree{
    // Trie node
    private class TrieNode{
        TrieNode[] children;
        boolean isEnd;


        TrieNode(){
            children = new TrieNode[26]; // 26 lowercase chars
            isEnd = false;
        }
        
    }

    private TrieNode root;

    public PrefixTree(){
        root = new TrieNode();
    }

    public void insert(String word){

        TrieNode current = root; 

        for(char c: word.toCharArray()){
            int index = c - 'a';
            
            // Create node if isn't exist
            if (current.children[index] == null){
                current.children[index]= new TrieNode();
            }

            //Move to children
            current = current.children[index];

        }

        //Mark end in word
        current.isEnd = true; 
    }

    public boolean search(String word){
        TrieNode node = findNode(word);

        // Must exist node and be end of word
        return node != null && node.isEnd;
    }


    public boolean startsWith(String prefix){
        //only verify if node exists
        return findNode(prefix) != null; 

    }

    private TrieNode findNode(String s){
        TrieNode current = root;

        for(char c: s.toCharArray()){

            int index = c - 'a';

            if(current.children[index] == null){
                return null;
            }

            current = current.children[index];
        }

        return current; 
    }
      
}

