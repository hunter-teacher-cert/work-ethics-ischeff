# This program was created (albeit clusmily) by Ian Scheffler

# /**
#    The Rules of Life:
#    Survivals:
#    * A cell with 2 or 3 living neighbours will survive for the next generation.
#    Death:
#    * Each cell with >3 neighbours will die from overpopulation.
#    * Every cell with <2 neighbours will die from isolation.
#    Birth:
#    * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.
#    NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation
# */

# initialize empty board (all cells dead)
def create_new_board(rows, cols):
    board = []
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(0)
        board.append(col)
    return board

# print the board to the terminal
def print_board(board):
    for row in board:
        for elem in row:
            print(elem, end = ' ')
        print()

# set a single cell  located at (rows, cols) to value val
def set_cell(board, rows, cols, val):
    board[rows][cols] = val

# return number of living neigbours of board[r][c]


# precond: given a board and a cell
# postcond: return next generation cell state based on CGOL rules
# (alive 'X', dead ' ')

# generate new board representing next generation

# pause for n milliseconds

# "repaint" by using an ANSI control character to
# repeatedly place the cursor at the origin (upper left)

# main function (written with python if name idiom)
if __name__ == '__main__':
    board1 = create_new_board(30, 30)
    print_board(board1)
    set_cell(board1, 0, 0, 1)
    print()
    print_board(board1)
