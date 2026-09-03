
class TrieNode:
    def __init__(self):
        self.hijos = {}
        self.es_fin = False 
class WordDictionary:

    def __init__(self):
        self.raiz= TrieNode()
      
        

    def addWord(self, word: str) -> None:
        node = self.raiz
        for letra in word:
            if letra not in node.hijos: 
                node.hijos[letra] = TrieNode()
            node = node.hijos[letra]

        node.es_fin = True 
 

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:

            #Caso base: llegamos final de palabra
            if index == len(word):
                return node.es_fin 


            letra = word[index]

            #Si es comodin, probar todos los hijos
            if letra == '.':
                for hijo in node.hijos.values():
                    if dfs(index + 1, hijo):
                        return True
                return False 


            #Si es letra normal, ir al hijo correspondiente
            else: 
                if letra not in node.hijos: 
                    return False
                return dfs(index+1, node.hijos[letra])


        return dfs(0, self.raiz)





