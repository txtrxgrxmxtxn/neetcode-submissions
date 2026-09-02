class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            # Si el carácter no existe, crear un nuevo nodo
            if char not in node.children:
                node.children[char] = TrieNode()
            # Avanzar al siguiente nodo
            node = node.children[char]
        
        # Marcar el final de la palabra
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            # Si el carácter no existe, la palabra no está
            if char not in node.children:
                return False
            node = node.children[char]
        
        # La palabra existe solo si terminamos en un fin de palabra
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            # Si el carácter no existe, no hay palabras con este prefijo
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Si llegamos aquí, el prefijo existe
        return True