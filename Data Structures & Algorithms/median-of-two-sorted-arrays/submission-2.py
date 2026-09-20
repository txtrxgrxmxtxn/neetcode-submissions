class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #paso 1: asegurar que num1 sea arreglo mas corto
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = m + n
        half = (total + 1) // 2 #tamaño mitad izq

        #paso 2: inicializar limites para busqueda binaria en nums1
        left = 0
        right = m 

        #paso 3: busqueda binaria 
        while left <= right: 
            #punto de particion nums1
            i = (left + right) // 2 
            #punto de particion en nums2 (compl)
            j = half - i

            #paso 4: obtener elementos alrededor de particion
            nums1_left = nums1[i-1] if i>0 else float('-infinity')
            nums1_right = nums1[i] if i<m else float('infinity')
            nums2_left = nums2[j-1] if j>0 else float('-infinity')
            nums2_right = nums2[j] if j<n else float('infinity')


            #paso 5: Verificar si particion correcta
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                #particion conrrecta encontrada
                #paso 6: calcular mediana
                if total % 2 == 1: #total impar
                    #la mediana es el maximo de los elementos izq
                    return max(nums1_left, nums2_left)
                else: #total par 
                    max_left = max(nums1_left, nums2_left)
                    min_right = min(nums1_right, nums2_right)
                    return(max_left + min_right)/2



            #paso 7: ajustar la busqueda si la particion no es correcta 
            elif nums1_left > nums2_right:
                #nums1_left es mas grande, mover i a izq
                right = i-1
            else:
                #nums2_left es demasiado grande, mover i hacia der.
                left = i+1

        return 0.0 