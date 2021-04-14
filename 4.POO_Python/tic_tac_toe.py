from random import randrange

def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    print('+-------+-------+-------+',sep='\n')
    for i in board:
        row = '|       |       |       |\n|'
        for j in i:
            row += f"   {j}   |"
        print(row, '|       |       |       |','+-------+-------+-------+', sep='\n')

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    cell = int(input('\nIngrese casilla donde hara su movimiento: '))
        
    # Obtenemos las casillas que estan disponible
    freeFields = MakeListOfFreeFields(board)

    # Recorremos el tablero con los indices de elementos solos
    for i in freeFields:
        if board[i[0]][i[1]] == cell:
            board[i[0]][i[1]] = 'O'
            return True
    return False
                


def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    freeFields = []
    for fila in range(0, len(board)):
        for col in range(0, len(board[fila])):
            if board[fila][col] != 'X' and board[fila][col] != 'O':
                freeFields.append((fila, col))
    
    return freeFields


def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    diagonal = 0
    # Verificando ganador por fila
    for i in range(0,3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True          
        # Segunda diagnonal
        if i == 2:
            if board[0][i] == sign and board[1][1] == sign and board[i][0] == sign:
                return True
        if board[i][i] == sign:
            diagonal += i
    if diagonal == 3:
        return True
    return False
    
    

def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    if board[1][1] != 'X':
        board[1][1] = 'X'
        return
    
    freeFields = MakeListOfFreeFields(board)
    cell = randrange(9)
    for i in freeFields:
        if board[i[0]][i[1]] == cell:
            board[i[0]][i[1]] = 'X'
            return 

    DrawMove(board)


def main():
    # Crear tablero lleno con numeros desde 1-9
    board = [[ i+(3*j) for i in range(1,4) ] for j in range(0,3)]
    
    # Mostrar tablero en pantalla
    print('JUEGO DE TIC TAC TOE')
    DisplayBoard(board)

    print("TURNO MAQUINA")
    DrawMove(board)
    DisplayBoard(board)

    for i in range (0,4):

        if VictoryFor(board,'O'):
            print("FELICIDADES HAZ GANADO!!! :D")
            break
        if VictoryFor(board,'X'):
            print("LO SIENTO HAS PERDIDO :(")
            break

        print("TURNO USUARIO")
        correct = False
        while not correct:
            correct = EnterMove(board)
        
        DisplayBoard(board)
        
        print("TURNO MAQUINA")
        DrawMove(board)
        DisplayBoard(board)
        
    
    if not VictoryFor(board,'O') and not VictoryFor(board,'X'):
        print("EMPATE :/")
    
main()