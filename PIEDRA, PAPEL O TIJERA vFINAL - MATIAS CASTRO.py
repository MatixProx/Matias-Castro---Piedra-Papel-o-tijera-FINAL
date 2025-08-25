import random

opciones = {1: "piedra", 2: "papel", 3: "tijera"}

while True:
    while True:
        print("Elige: 1. Piedra, 2. Papel, 3. Tijera")
        entrada = input("Tu elección: ")
        if entrada not in ("1", "2", "3"):
            print("Opción inválida, intenta de nuevo.\n")
            continue

        jugada = int(entrada)
        jugador = opciones[jugada]
        computadora = opciones[random.randint(1, 3)]
        print(f"Tú elegiste {jugador}, la computadora eligió {computadora}.")

        if jugador == computadora:
            print("Empate, ambos volverán a elegir...\n")
            continue
        break

    if (jugador == "piedra" and computadora == "tijera") or \
       (jugador == "papel" and computadora == "piedra") or \
       (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!\n")
    else:
        print("¡Perdiste!\n")
