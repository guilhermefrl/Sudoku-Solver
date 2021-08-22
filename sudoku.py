"""
Sodoku Solver
"""
import sys

EMPTY = 0
TAM = 9

def main():

    # Assegurar o uso correto
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 sudoku.py file.txt")

    # Guardar nome do ficheiro
    filename = 'examples/' + sys.argv[1]

    # Ler ficheiro
    board, valid = read_file(filename)

    # Erro
    if valid == False:
        sys.exit("Error! Was not possible to open the folder or didn't meet the requirements.")

    # Mostrar tabuleiro inicial
    print_board(board)

    # Resolver tabuleiro de sudoku
    solve_sudoku(board)

    # Mostrar resolução
    print_board(board)
                

def read_file(filename):
    """
    Retorna uma matriz e True caso seja possível ler o ficheiro, caso contrário retorna False
    """
    # Iniciar tabuleiro
    board = initial_state()

    i=0
    j=0
    aux=0

    # Abrir ficheiro
    with open(filename) as file:
        lines = file.readlines()

        # Ler o ficheiro para o array
        for line in lines:
            j = 0
            for char in line:
                if char != " " and char != "|" and char != "\n" and char != "-" and j < 9:
                    if char == ".":
                        board[i][j] = EMPTY
                        j += 1
                    elif int(str(char)) > 0 and int(str(char)) < 10:
                        board[i][j] = int(str(char))
                        j += 1

            aux += 1

            if(aux != 4 and aux != 8 and i < 9):
                i += 1

        # Caso seja válida
        if aux == 11 and j == 9:
            return board, True
        # Caso não seja válida
        else:
            return None, False


def initial_state():
    """
    Retorna o estado inicial do tabuleiro.
    """
    return [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]


def solve_sudoku(board):
    """
    Função que resolve o sudoku.
    """

    # Encontrar um lugar vazio no tabuleiro
    exists, row, col = find_empty_space(board)

    # Caso não existam mais lugares vazios, então foi resolvido o sudoku, visto que foi apenas permitido inserir números válidos
    if exists == False:
        return True

    # Caso exista um lugar para colocar o número, tentar com um número de 1 a 9
    for number in range(1, TAM+1):

        # Verificar se é possível colocar o número nessa posição
        if valid_move(board, row, col, number):
            # Fazer a tentativa
            board[row][col] = number

            # Chamar recursivamente a função, caso retorne True é porque foi encontrada a solução
            if(solve_sudoku(board)):
                return True

            # Caso não seja resolvido o sudoku com esse número
            board[row][col] = EMPTY

    # Para continuar a fazer backtracking
    return False


def find_empty_space(board):
    """
    Retorna True e a posição, caso exista um lugar vazio, caso contrário retorna False
    """

    for i in range(TAM):
        for j in range(TAM):
            # Caso exista uma posição sem número
            if board[i][j] == EMPTY:
                return True, i, j

    return False, None, None


def valid_move(board, row, col, number):
    """
    Retorna True seja possível colocar o número, caso contrário retorna False.
    """

    # Verificar todas as condições, para colocar o número nessa posição
    if check_row(board, row, number) and check_col(board, col, number) and check_subgrid(board, row, col, number):
        return True
    else:
        return False


def check_row(board, row, number):
    """
    Retorna True seja possível colocar o número na linha, caso contrário retorna False.
    """

    for j in range(TAM):
        # Caso já exista esse número na linha
        if board[row][j] == number:
            return False

    return True


def check_col(board, col, number):
    """
    Retorna True seja possível colocar o número na coluna, caso contrário retorna False.
    """

    for i in range(TAM):
        # Caso já exista esse número na coluna
        if board[i][col] == number:
            return False

    return True


def check_subgrid(board, row, col, number):
    """
    Retorna True seja possível colocar o número no subgrupo, caso contrário retorna False.
    """

    # Verificar qual é o subgrupo
    row_sg = (row // 3) * 3
    col_sg = (col // 3) * 3

    for i in range(row_sg, row_sg+3):
        for j in range(col_sg, col_sg+3):
            # Caso já exista esse número no subgrupo
            if board[i][j] == number:
                return False

    return True


def print_board(board):
    """
    Mostra o tabuleiro de sudoku
    """
    aux = 0
    aux1 = 0

    print("|-------|-------|-------|")

    for i in range(TAM):
        print("|", end=" ")
        for j in range(TAM):
            if board[i][j] == EMPTY:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")

            aux += 1

            if (aux == 3):
                print("|", end=" ")
                aux = 0

        print()

        aux1 += 1

        if (aux1 == 3):
            print("|-------|-------|-------|")
            aux1 = 0

    print()


if __name__ == "__main__":
    main()