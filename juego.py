import random
jugador = input("Ingrese su jugada: ")
jugadas = ["piedra", "papel", "tijera"]
machine = jugadas[random.randint(0,2)]
print("maquia: ", machine)

if jugador == "piedra" and machine == "tijera" or jugador == "papel" and machine == "piedra" or jugador == "tijera" and machine == "papel":
    print("GANASTE")
elif machine == "piedra" and jugador == "tijera" or machine == "papel" and jugador == "piedra" or machine == "tijera" and jugador == "papeL":
    print("PERDISTE")
else:
    print ("FIN DEL JUEGO")