class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #tarea 1: preparar los datos
        cars = sorted(zip(position, speed), key= lambda x : x[0], reverse = True )
        #tarea 2:Inicializar contador y tiempo anterior
        fleet_count = 0
        prev_time = 0 #t. del ult. fleet formado (el de adelante)


        #tarea 3 y 4: procesar cada auto de adelante hacia atrás
        for pos, spd in cars: 
            #calc. t. de llegada de este auto.
            time = (target - pos) / spd 

            #Si este auto tarda más que el fleet de adelante 
            #Entonces no lo alcanza y forma nuevo fleet

            if time > prev_time: 
                fleet_count += 1
                prev_time = time 


            #si time <= prev_time, se une al fleet de adelante y no hacemos nada

        #tarea 5: retornar resultado

        return fleet_count
        