# Plot the game board on screen.
from string import Template
from os import system


def show_game_board(board, player):
    # Clear the screen before every plot.
    system("cls")

    print("*** JOGO DA VELHA ***\n")

    # Printing the contents of the board matrix on the screen.
    board_print = Template("$a | $b | $c\n$d | $e | $f\n$g | $h | $i")

    print(
        board_print.substitute(
            a=board[0][0],
            b=board[0][1],
            c=board[0][2],
            d=board[1][0],
            e=board[1][1],
            f=board[1][2],
            g=board[2][0],
            h=board[2][1],
            i=board[2][2],
        )
    )

    # "Pausing" the program execution.
    input("\nAperte qualquer tecla para contiunar.")


# Buld the game board.
def build_board():
    # The board is a 3x3 matrix.
    board = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]
    return board


# Update the fields in the board.
def mark_field(board, initial_marks, pl_mark):

    # First itercation to star the turn.
    aux_mark = mark_menu(initial_marks)

    # Check if the selected field is already filled.
    # Only goes forward if the selected field is empty.
    while board[aux_mark[0]][aux_mark[1]] not in initial_marks:

        print("\nEscolha outra posição!")

        aux_mark = mark_menu(initial_marks)

    # The selected field gets the player mark.
    board[aux_mark[0]][aux_mark[1]] = pl_mark


# Marks menu.
def mark_menu(initial_marks):
    # Clear the screen.
    system("cls")

    mark = ()

    # Positions menu.
    positions = (
        (),
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    )

    # Print the menu options on screen.
    print("** Posições **")
    print("1 - A1\n2 - A2\n3 - A3\n4 - B1\n5 - B2\n6 - B3\n7 - C1\n8 - C2\n9 - C3\n")

    # User option input.
    rec_mark = int(
        input("Informe a posição que deseja marcar (pelo número): "))

    mark = positions[rec_mark]

    return mark


# Play the turns.
def play_turns(board):

    # Printing the player.
    player_print = Template("Jogador da rodada: $pl\n Marcador: $mk\n")

    print(player_print.substitute(pl=player[0], mk=player[1]))


# Formatting the players.
def player(players):

    # Array to put together the player name and the mark it'll be used.
    aux_var = []
    get_mark = ""
    mark_array = ["X", "x", "O", "o"]
    
    # Player's name goes to position 0.
    aux_var.append(input("Informe seu nome: ").capitalize())
    
    # Player's mark goes to position 1.
    get_mark = input(
        "\nVocê vai jogar com X ou O?\n Informe o marcador selecionado: ")

    # Get size of players array.
    tam = len(players)

    # "tam < 1" mean that is the first entry, or player 1 choice.
    if tam < 1:
        # Check if the selected mark is X or O.
        # Does not accept any different value.
        while True:
            if get_mark in mark_array:
                break
            else:
                print("Marcador inválido! Selecione outro!\n")
                get_mark = input(
                    "Você vai jogar com X ou O?\n Informe o marcador selecionado: "
                )
    else:
        # Check if the selected mark is X or O.
        # Does not accept any different value.
        while True:
            if get_mark in mark_array:
                # Check if the mark is disponible.
                if players[0][1] == get_mark:
                    print("Marcador inválido! Selecione outro!\n")
                    get_mark = input(
                        "Você vai jogar com X ou O?\n Informe o marcador selecionado: "
                    )
                else:
                    break
            else:
                print("Marcador inválido! Selecione outro!\n")
                get_mark = input(
                    "Você vai jogar com X ou O?\n Informe o marcador selecionado: "
                )

    # Turns the mark input into a uppercase value to maintain the same pattern during the game.
    aux_var.append(get_mark.upper())

    return aux_var


# Main program.
# Global imports.


# Global variables.
initial_marks = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
board = build_board()  # Board game.
players = []


# Input player 1 and player 2.
players.append(player(players))
players.append(player(players))

show_game_board(board, players[0])
mark_field(board, initial_marks, players[0][1])

show_game_board(board, players[0])
