
from funciones import *
from variables import *
import random
import time

tablero_maquina = crear_tablero(10)
tablero_jugador = crear_tablero(10)
tablero_disparos = crear_tablero(10)

#Se pintan los barcos en los tableros(maquina y humano) 
tablero_jugador = pintar_barcos(barcos_jh,tablero_jugador)
tablero_maquina = pintar_barcos(barcos_m,tablero_maquina)
print("COMIENZA EL JUEGO...")
print()

print("TABLERO JUGADOR")
imprimir_tablero(tablero_jugador)
print()
print("REGISTRO DE DISPAROS HUMANOS")
imprimir_tablero(tablero_disparos)
print()
print("ATENTO, se te pedirá una coordenada (x,y), se admiten sólo numeros del 0 a 10. Si te equivocas perderás el turno.")


continuar = True

while continuar:
    try:
        print()
        jugada_humana(tablero_maquina,tablero_disparos)
        if buscando_barcos(tablero_maquina) == False:
            print("Felicidades! Has derribado todo los barcos. Salvaste la raza humana")
            break
        else:
            jugada_maquina(tablero_jugador)
            print("Tu tablero ha quedado la siguiente forma:")
            imprimir_tablero(tablero_jugador)
            if buscando_barcos(tablero_jugador) == False:
                print("La máquina ha derribado todos tus barcos.")
                continuar = False
            else:
                continue
    except Exception as e:
        print(f"Ocurrió un error : SOS UN IMBECIL")