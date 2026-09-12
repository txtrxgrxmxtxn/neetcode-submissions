class PrefixTree {
    // Nodo del Trie
    private class TrieNode {
        TrieNode[] children;
        boolean isEnd;
        
        TrieNode() {
            children = new TrieNode[26];  // 26 letras minúsculas
            isEnd = false;
        }
    }
    
    private TrieNode root;
    
    public PrefixTree() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode current = root;
        
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            
            // Crear el nodo si no existe
            if (current.children[index] == null) {
                current.children[index] = new TrieNode();
            }
            
            // Moverse al hijo
            current = current.children[index];
        }
        
        // Marcar fin de palabra
        current.isEnd = true;
    }
    
    public boolean search(String word) {
        TrieNode node = findNode(word);
        // Debe existir el nodo y ser fin de palabra
        return node != null && node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        // Solo verificar que el nodo exista
        return findNode(prefix) != null;
    }
    
    // Método auxiliar: navega el Trie y retorna el nodo final
    private TrieNode findNode(String s) {
        TrieNode current = root;
        
        for (char c : s.toCharArray()) {
            int index = c - 'a';
            
            if (current.children[index] == null) {
                return null;
            }
            
            current = current.children[index];
        }
        
        return current;
    }
}