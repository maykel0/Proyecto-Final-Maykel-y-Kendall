import random

lst_informacionPlayer1 = []
lst_informacionPlayer2 = []

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

tablero_Player1 = [
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
]
tablero_Player2 = [
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
]

tablero_visible1 = [
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
]
tablero_visible2 = [
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
]


class Jugador:
    def __init__(self, pnombre, pnaves_vehiculos, pmunicion):
        self.nombre = pnombre
        self.naves_vehiculos = pnaves_vehiculos
        self.municion = pmunicion

    def mostrar_nombre(self):
        print(f"{self.nombre}")

    def restar_naves_vehiculos(self):
        self.naves_vehiculos["Naves/Vehiculos"] -= 1

    def restar_municion(self):
        longitud = len(self.municion)
        self.municion.remove(self.municion[longitud - 1])

    def mostrar_municion(self):
        total = 0
        for i in range(len(self.municion)):
            total += self.municion[i]
        print(f"{total}")

    def mostrar_naves_vehiculos(self):
        print(f"{self.naves_vehiculos}")

    def tiro_fallido(self):
        longitud = len(self.municion)
        self.municion[longitud - 1] = self.municion[longitud - 1] - 1

    def n_naves_vehiculos(self):
        return self.naves_vehiculos

    def retornar_municion(self):
        total = 0
        for i in range(len(self.municion)):
            total += self.municion[i]
        return total


def nombres_jugadores():
    print(f"{GREEN}{BOLD}--------------------Ingrese el Nombre del Jugador---------------------{RESET}")
    while True:
        player = input(f"{YELLOW}{BOLD}-------Jugador: {RESET}")
        if player == "" or player == " ":
            print(f"{RED}{BOLD}Tiene que ingresar un nombre{RESET}")
        else:
            break
    # Inplementar un comando para limpiar la pantalla
    return player


def add_ship(player1, player2):
    global lst_informacionPlayer1
    global lst_informacionPlayer2
    global tablero_Player1
    global tablero_Player2
    vehiculos1 = player1.n_naves_vehiculos()
    naves1 = player2.n_naves_vehiculos()
    lst_informacionPlayer1.append(vehiculos1["Naves/Vehiculos"])
    lst_informacionPlayer2.append(naves1["Naves/Vehiculos"])
    lst_informacionPlayer1.append(0)
    lst_informacionPlayer2.append(0)

    while True:
        for i in range(vehiculos1["Naves/Vehiculos"]):
            while True:
                ship_column = random.randint(0, 4)
                ship_row = random.randint(0, 4)
                if tablero_Player1[ship_column][ship_row] == "[ ]":
                    tablero_Player1[ship_column][ship_row] = "[s]"
                    break
        break

    while True:
        for i in range(naves1["Naves/Vehiculos"]):
            while True:
                ship_column = random.randint(0, 4)
                ship_row = random.randint(0, 4)
                if tablero_Player2[ship_column][ship_row] == "[ ]":
                    tablero_Player2[ship_column][ship_row] = "[s]"
                    break
        break


def naves():
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(
        f"{GREEN}{BOLD}-------------------------{BLUE}Juegas con naves{GREEN}-----------------------------{RESET}")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    ships = random.randint(5, 10)
    print(f"Se han generado {ships} naves-----------------------------------------------")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    input(f"{WHITE}{BOLD}Presione enter para continuar{RESET}")
    diccionario = {
        "Naves/Vehiculos": ships
    }
    return diccionario


def vehiculos():
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(
        f"{GREEN}{BOLD}-------------------------{BLUE}Juegas con vehiculos{GREEN}-------------------------{RESET}")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    vehicules = random.randint(5, 10)
    print(f"Se han generado {vehicules} vehiculos------------------------------------------")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    input(f"{WHITE}{BOLD}Presione enter para continuar{RESET}")
    diccionario = {
        "Naves/Vehiculos": vehicules
    }
    return diccionario


def weapon(nnaves_vehiculos):
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    attacks = []
    total = 0
    for i in range(nnaves_vehiculos["Naves/Vehiculos"]):
        attacks.append(random.randint(1, 5))
    for i in range(len(attacks)):
        total += attacks[i]
    print(f"El jugador posee {total} ataques-------------------------------------------{RESET}")
    return attacks


def tablero_jugador1():
    print("Tablero del Jugador 1")
    for i in range(5):
        print(tablero_Player1[i])


def tablero_jugador2():
    print("Tablero del Jugador 2")
    for i in range(5):
        print(tablero_Player2[i])


def crear_jugadores():
    nombre = nombres_jugadores()
    nvehiculos = vehiculos()
    player1 = Jugador(nombre, nvehiculos, weapon(nvehiculos))
    nombre = nombres_jugadores()
    nnaves = naves()
    player2 = Jugador(nombre, nnaves, weapon(nnaves))
    return player1, player2


def mostrar_nombres(player1, player2):
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"{YELLOW}{BOLD}-------Jugador 1: {RESET}"), player1.mostrar_nombre()
    print(f"{YELLOW}{BOLD}-------Jugador 2: {RESET}"), player2.mostrar_nombre()
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    input("Presione enter para continuar")


def turno_jugador2(player1, player2):
    opcion = 0
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"{GREEN}{BOLD}----------------------Ingrese una opcion a seguir---------------------{RESET}")
    print(f"{GREEN}{BOLD}--------------------------Opcion 1: atacar----------------------------{RESET}")
    print(f"{GREEN}{BOLD}--------------------------Opcion 2: rendirse--------------------------{RESET}")
    while True:
        try:
            opcion = int(input())
        except ValueError:
            print("")

        if opcion == 1 or opcion == 2:
            break

        else:
            print("Ingrese una opcion valida")

    if opcion == 2:
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"Te has rendido la victoria es del jugador numero 1 ")
        player1.mostrar_nombre()
        return 2

    if opcion == 1:
        for fila in range(5):
            print(tablero_visible2[fila])
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print("Municion actual: "), player2.mostrar_municion()
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        while True:
            while True:
                try:
                    posicion1 = int(input("Ingresa la posicion 1 (0 - 4): "))
                    if posicion1 >= 5 or posicion1 <= -1:
                        print("Opcion fuera del rango")

                    elif posicion1 <= 5 and posicion1 >= -1:
                        break
                except ValueError:
                    print("Ingrese un valor numerico")

            while True:
                try:
                    posicion2 = int(input("Ingresa la posicion 2 (0 - 4): "))

                    if posicion2 >= 5 or posicion2 <= -1:
                        print("Opcion fuera del rango")

                    elif posicion2 <= 5 and posicion2 >= 0:
                        break
                except ValueError:
                    print("Ingrese un valor numerico")

            if tablero_Player1[posicion1][posicion2] == "[ ]":
                print("Fallaste el espacio estaba vacio")
                tablero_visible2[posicion1][posicion2] = "[x]"
                tablero_Player1[posicion1][posicion2] = "[x]"
                player2.tiro_fallido()
                print("Municion actual:")
                player2.mostrar_municion()
                break

            elif tablero_Player1[posicion1][posicion2] == "[s]":
                print("Destruiste un tanques enemigo")
                tablero_Player1[posicion1][posicion2] = "[X]"
                tablero_visible2[posicion1][posicion2] = "[X]"
                player1.restar_municion()
                player1.restar_naves_vehiculos()
                player2.tiro_fallido()
                print("Municion actual:")
                player2.mostrar_municion()
                municion1 = player1.retornar_municion()
                municion2 = player2.retornar_municion()
                vehiculo = player1.n_naves_vehiculos()
                nave = player2.n_naves_vehiculos()
                contador1()
                if municion1 * 1.7 < municion2 or vehiculo["Naves/Vehiculos"] * 1.8 < nave["Naves/Vehiculos"]:
                    print("Victoria de:")
                    player2.mostrar_nombre()
                    return 2
                else:
                    return 1
            elif tablero_Player1[posicion1][posicion2] == "[X]" or tablero_Player1[posicion1][posicion2] == "[x]":
                print("ya habias disparado en esta posicion, vuelve a fijar las cordenadas")

        return opcion


def turno_jugador1(player1, player2):
    opcion = 0
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"{GREEN}{BOLD}----------------------Ingrese una opcion a seguir---------------------{RESET}")
    print(f"{GREEN}{BOLD}--------------------------Opcion 1: atacar----------------------------{RESET}")
    print(f"{GREEN}{BOLD}--------------------------Opcion 2: rendirse--------------------------{RESET}")
    while True:
        try:
            opcion = int(input())
        except ValueError:
            print("")

        if opcion == 1 or opcion == 2:
            break

        else:
            print("Ingrese una opcion valida")

    if opcion == 2:
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"Te has rendido la victoria es del jugador numero 2 ")
        player2.mostrar_nombre()
        return 2

    if opcion == 1:
        for fila in range(5):
            print(tablero_visible1[fila])
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print("Municion actual: "), player1.mostrar_municion()
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        while True:
            while True:
                try:
                    posicion1 = int(input("Ingresa la posicion 1 (0 - 4): "))
                    if posicion1 >= 5 or posicion1 <= -1:
                        print("Opcion fuera del rango")

                    elif posicion1 <= 5 and posicion1 >= -1:
                        break
                except ValueError:
                    print("Ingrese un valor numerico")

            while True:
                try:
                    posicion2 = int(input("Ingresa la posicion 2 (0 - 4): "))

                    if posicion2 >= 5 or posicion2 <= -1:
                        print("Opcion fuera del rango")

                    elif posicion2 <= 5 and posicion2 >= 0:
                        break
                except ValueError:
                    print("Ingrese un valor numerico")

            if tablero_Player2[posicion1][posicion2] == "[ ]":
                print("Fallaste el espacio estaba vacio")
                tablero_visible1[posicion1][posicion2] = "[x]"
                tablero_Player2[posicion1][posicion2] = "[x]"
                player1.tiro_fallido()
                print("Municion actual:")
                player1.mostrar_municion()
                break

            elif tablero_Player2[posicion1][posicion2] == "[s]":
                print("Destruiste una nave enemiga")
                tablero_Player2[posicion1][posicion2] = "[X]"
                tablero_visible1[posicion1][posicion2] = "[X]"
                player2.restar_municion()
                player2.restar_naves_vehiculos()
                player1.tiro_fallido()
                print("Municion actual:")
                player1.mostrar_municion()
                municion1 = player2.retornar_municion()
                municion2 = player1.retornar_municion()
                vehiculo = player2.n_naves_vehiculos()
                nave = player1.n_naves_vehiculos()
                contador2()
                if municion1 * 1.7 < municion2 or vehiculo["Naves/Vehiculos"] * 1.8 < nave["Naves/Vehiculos"]:
                    print("Victoria de:")
                    player1.mostrar_nombre()
                    return 2
                else:
                    return 1
            elif tablero_Player2[posicion1][posicion2] == "[X]" or tablero_Player2[posicion1][posicion2] == "[x]":
                print("ya habias disparado en esta posicion, vuelve a fijar las cordenadas")

        return opcion


def contador1():
    global lst_informacionPlayer1
    lst_informacionPlayer1[1] += 1


def contador2():
    global lst_informacionPlayer2
    lst_informacionPlayer2[1] += 1


def resultados():
    return lst_informacionPlayer1, lst_informacionPlayer2
