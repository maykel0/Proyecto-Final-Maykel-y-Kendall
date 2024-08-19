import Juego

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


def menu():
    player1, player2 = Juego.crear_jugadores()
    Juego.mostrar_nombres(player1, player2)
    Juego.add_ship(player1, player2)
    while True:
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print("Turno del jugador 1")
        ciclo = Juego.turno_jugador1(player1, player2)
        if ciclo == 2:
            break
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print("Turno del Jugador 2")
        ciclo = Juego.turno_jugador2(player1, player2)
        if ciclo == 2:
            break
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    lst_informacionplayer1, lst_informacionplayer2 = Juego.resultados()
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"El jugador 1 tenia: {BOLD}{CYAN}{lst_informacionplayer1[0]}{RESET} vehiculos, y se destruyeron: {BOLD}{YELLOW}{lst_informacionplayer1[1]}{RESET}")
    print(f"El jugador 2 tenia: {BOLD}{CYAN}{lst_informacionplayer2[0]}{RESET} vehiculos, y se destruyeron: {BOLD}{YELLOW}{lst_informacionplayer2[1]}{RESET}")
    print(f"En total se destruyeron {lst_informacionplayer1[1] + lst_informacionplayer2[1]} naves y vehiculos")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"{BOLD}{BLUE}Gracias por jugar....{RESET}")


if __name__ == "__main__":
    while True:

        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"{GREEN}{BOLD}---------Bienvenido al Menu de Inicio de Guerra De Los Mundos---------{RESET}")
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        print(f"{GREEN}{BOLD}----------------------------------------------------------------------{RESET}")
        while True:
            juego = input(f"{YELLOW}{BOLD}Escriba S para empezar a jugar, cualquier otra tecla cerrara el juego: {RESET}")

            if juego == "s":
                menu()
                break
            else:
                break

        break
