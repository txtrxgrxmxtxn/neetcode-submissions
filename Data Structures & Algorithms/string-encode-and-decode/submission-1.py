class Solution:

    def encode(self, strs: List[str]) -> str:

        #Lista para string codificado
        encoded=[]

        #codificar cada string con formato: longitud#string
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)


        #unir todo
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        #lista para strings decodificados
        result=[]

        #indice para recorrer string decodificado
        i=0

        while i<len(s):
            #encontrar la posición del delimitador '#'
            j=i
            while s[j] != '#':
                j+=1

            #extraer longitud de string
            length = int(s[i:j])


            #calcular inicio y fin del string 
            start = j+1
            end= start + length 

            #extraer el string + agregarlo al resultado
            result.append(s[start:end])


            #mover el indice al siguiente string codificado
            i= end
        return result




