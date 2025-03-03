# La libreria [sys.exit] nos permitira salir del juego, cuando el usuario desee salir
import sys
# Se debe importar la libreria de [random] para permitir a la maquina seleccionar una las opciones del jueego
import random
def mostrar_menu():
    """Se crea una funcion para el menu principal del juego
    donde se muestra las opciones
    1. Jugar
    2. Reglas del juego
    3. Salir"""
    estadisticas = {"jugadas": 0, "ganadas": 0, "perdidas": 0, "empatadas": 0}
    while True:
        print("\nMenú Principal")
        print("1. Jugar")
        print("2. Reglas del Juego")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_submenu_jugar(estadisticas)
        elif opcion == "2":
            mostrar_reglas(estadisticas)
        elif opcion == "3":
            print("Saliendo del juego...")
            sys.exit()
        else:
            print("Opción no válida, intenta de nuevo.")

def mostrar_submenu_jugar(estadisticas):
    """ Se crea una funcion para el submenu, dodne se muestran los modos de juego y las estadisticas
        1. Contra la maquina   
        2. Multijugador
        3. Estadisticas
        4. Volver al menu principal
    """
    while True:
        print("\nSelecciona el modo de juego:")
        print("1. Contra la máquina")
        print("2. Multijugador")
        print("3. Estadísticas")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Modo 'Contra la Máquina' seleccionado.")
            jugar_contra_maquina (estadisticas)
            
        elif opcion == "2":
            print("Modo 'Multijugador' seleccionado.")
            modo_muljugador (estadisticas)
            
        elif opcion == "3":
            print("Mostrando estadísticas...")
            mostrar_estadisticas(estadisticas)
        elif opcion == "4":
            return
        else:
            print("Opción no válida, intenta de nuevo.")
def mostrar_reglas():
    """Muestra las reglas básicas del juego:
    - Piedra vence a Tijera.
    - Tijera vence a Papel.
    - Papel vence a Piedra.
    - Si ambos jugadores eligen la misma opción, es un empate.
    """
    print("\nReglas del Juego:")
    print("- Piedra vence a Tijera.")
    print("- Tijera vence a Papel.")
    print("- Papel vence a Piedra.")
    print("- Si ambos jugadores eligen la misma opción, es un empate.")

def jugar_contra_maquina (estadisticas):
    """
     Ejecuta el modo de jueego contra la máquina.
    """
    jugador = str(input("Ingrese su nombre: "))
    num_partidas = int(input("Ingrese el número de partidas que desea jugar: "))
    for _ in range(num_partidas):
        jugadas = ["piedra", "papel", "tijera"]
        jugador = str(input("Ingrese su jugada, ya sea piedra, papel o tijera: "))
        machine = random.choice(jugadas)
        print("maquina: ", machine)
        # Condicionales que permiten seleccionar como ganador al usuario
        if jugador == "piedra" and machine == "tijera" or jugador == "papel" and machine == "piedra" or jugador == "tijera" and machine == "papel":
            print("GANASTE")
            estadisticas["ganadas"] += 1
        # Condicionales que permite seleccionar como ganador al pc    
        elif machine == "piedra" and jugador == "tijera" or machine == "papel" and jugador == "piedra" or machine == "tijera" and jugador == "papel":
            print("PERDISTE")
            estadisticas["perdidas"] += 1
        else:
            print ("EMPATE")
            estadisticas["empatadas"] += 1
def modo_muljugador (estadisticas):
    """
    Ejecuta el modo de juego entre dos jugadores.
    """
    print("Modo multijugador seleccionado")
    jugador1 = str(input("Jugador 1 ingrese su nombre: "))
    jugador2 = str(input("Jugador 2 ingrese su nombre: "))
    num_partidas = int(input("Ingrese el número de partidas que desea jugar: "))
    for _ in range(num_partidas):
       jugada1 = input(f"{jugador1}, ingrese su jugada (piedra, papel o tijera): ").lower()
       print("\n" * 50)
       jugada2 = input(f"{jugador2}, ingrese su jugada (piedra, papel o tijera): ").lower()
       print (jugador1 ,"eligio: ",jugada1)
       print (jugador2 ,"eligio: ",jugada2)
       if jugada1 == jugada2:
        print ("EMPATE")
       elif jugada2 == "piedra" and jugada1 == "tijera" or jugada2 == "tijera" and jugada1 == "papel" or jugada2 == "papel" and jugada1 == "piedra":
        print("Gana ",jugador2)
        estadisticas["ganadas"] += 1
       else:
        print("Gana ",jugador1)
        estadisticas["perdidas"] += 1
def mostrar_estadisticas(estadisticas):
    """Ejecuta las funcion para recopilar las estadisticas segun los modos de juego"""
    print("\nEstadísticas del juego:")
    print(f"Partidas jugadas: {estadisticas['jugadas']}")
    print(f"Partidas ganadas: {estadisticas['ganadas']}")
    print(f"Partidas perdidas: {estadisticas['perdidas']}")
    print(f"Partidas empatadas: {estadisticas['empatadas']}")

if __name__ == "__main__":
    mostrar_menu()