class Nodo:
    def __init__(self, clave = 0, valor = 0):
        self.clave = clave
        self.valor = valor
        self.prev = None
        self.next = None 


class LRUCache:

    def __init__(self, capacity: int):
        #Guardar capacidad
        #Crear nodos dummy (cabeza y cola) conectados entre si 
        #inicializar diccionario
        self.capacidad = capacity
        self.cache = {} 

        #Nodos dummy 
        self.cabeza = Nodo() #Más reciente 
        self.cola = Nodo() #Más antiguo
        self.cabeza.next = self.cola
        self.cola.prev = self.cabeza 

    def _eliminar_nodo(self, nodo: Nodo) -> None: 

        """ Eliminar un nodo de la lista enlazada. """

        nodo.prev.next = nodo.next
        nodo.next.prev = nodo.prev


    def _agregar_al_frente(self, nodo: Nodo) -> None:
        """ Agregar nodo justo despues de la cabeza """
        nodo.next = self.cabeza.next
        nodo.prev = self.cabeza 
        self.cabeza.next.prev = nodo 
        self.cabeza.next = nodo 
        

    def get(self, key: int) -> int:
        #Si key no está en cache ----> -1 
        #Si está, mover el nodo al frente (mas reciente) y retornar valor 

        if key not in self.cache: 
            return -1 


        nodo = self.cache[key]
        #Mover al frente mas reciente
        self._eliminar_nodo(nodo)
        self._agregar_al_frente(nodo)

        return nodo.valor 

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            #Actualizar y mover frente
            nodo = self.cache[key]
            nodo.valor = value 
            self._eliminar_nodo(nodo)
            self._agregar_al_frente(nodo)
        else: 
            #Crear nuevo nodo
            nuevo_nodo = Nodo(key, value)
            self.cache[key] = nuevo_nodo
            self._agregar_al_frente(nuevo_nodo)



            #Si excede capacidad, eliminar menos reciente
            if len(self.cache) > self.capacidad:
                lru = self.cola.prev 
                self._eliminar_nodo(lru)
                del self.cache[lru.clave] 










        
