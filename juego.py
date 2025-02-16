# La libreria [sys.exit] nos permitira salir del juego, cuando el usuario desee salir
import sys
# Se debe importar la libreria de [random] para permitir a la maquina seleccionar una las opciones del jueego
import random
def mostrar_menu():
    """ Se crea una funcion para el menu principal
        1. Jugar
        2. Reglas
        3. Salir
    """
    while True:
        print("\nMenú Principal")
        print("1. Jugar")
        print("2. Reglas del Juego")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_submenu_jugar()
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("Saliendo del juego...")
            sys.exit()
        else:
            print("Opción no válida, intenta de nuevo.")

def mostrar_submenu_jugar():
    """ Se crea una funcion para el submenu, dodne se muestran los modos de juego y las estadisticas
        1. Contra el jugador
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
            jugar_contra_maquina ()
            # Llamar a la función correspondiente
        elif opcion == "2":
            print("Modo 'Multijugador' seleccionado.")
            modo_muljugador ()
            # Llamar a la función correspondiente
        elif opcion == "3":
            print("Mostrando estadísticas...")
            # Llamar a la función correspondiente
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

def jugar_contra_maquina ():
    """
     Ejecuta el modo de jueego contra la máquina.
    """
    num_partidas = int(input("Ingrese el número de partidas que desea jugar"))
    for _ in range(num_partidas):
        jugadas = ["piedra", "papel", "tijera"]
        jugador = str(input("usuario_mainIngrese su jugada, ya sea piedra, papel o tijera: "))
        machine = random.choice(jugadas)
        print("maquina: ", machine)
        # Condicionales que permiten seleccionar como ganador al usuario
        if jugador == "piedra" and machine == "tijera" or jugador == "papel" and machine == "piedra" or jugador == "tijera" and machine == "papel":
            print("GANASTE")
        # Condicionales que permite seleccionar como ganador al pc    
        elif machine == "piedra" and jugador == "tijera" or machine == "papel" and jugador == "piedra" or machine == "tijera" and jugador == "papel":
            print("PERDISTE")
        else:
            print ("EMPATE")
def modo_muljugador ():
    """
    Ejecuta el modo de juego entre dos jugadores.
    """
    print("Modo multijugador seleccionado")
    num_partidas = int(input("Ingrese el número de partidas que desea jugar"))
    for _ in range(num_partidas):
       jugador1 = str(input("Jugador1, ingrese su jugada: pidra, papel, tijera: " ))
       print("\n" * 50)
       jugador2 = str(input("Jugador2, ingrese su jugada: piedra, papel, tijera: " ))
       print ("Jugador1 eligio: ",jugador1)
       print ("Jugador2 eligio: ",jugador2)
       if jugador1 == jugador2:
        print ("EMPATE")
       elif jugador2 == "piedra" and jugador1 == "tijera" or jugador2 == "tijera" and jugador1 == "papel" or jugador2 == "papel" and jugador1 == "piedra":
        print("GANA JUGADOR 2")
       else:
        print("GANA JUGADOR 1")
if __name__ == "__main__":
    mostrar_menu()