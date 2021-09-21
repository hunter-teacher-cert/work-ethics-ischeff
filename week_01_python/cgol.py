# This program was created (albeit clusmily) by Ian Scheffler, with contributions by Jiyoon Kim,
# in particular with the count_neighbors function

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
            col.append(' ')
        board.append(col)
    return board

# print the board to the terminal
def print_board(board):
    for row in board:
        for elem in row:
            print(elem, end = ' ')
        print()

# set a single cell located at (rows, cols) to value val
def set_cell(board, rows, cols, val):
    board[rows][cols] = val

# return number of living neigbours of board[r][c]
def count_neighbours(board, rows, cols):
    #target = board[rows][cols]
    sum = 0
    startCol = cols - 1
    endCol = cols + 1
    startRow = rows - 1
    endRow = rows + 1
    # note: the following lines, which resolve issues of
    # running off the board, were inspired by Jiyoon Kim's solution
    #most top row
    if (rows == 0 and cols !=0 and cols != len(board[0]) - 1):
        startRow = rows;
    #most left col
    elif (cols == 0 and rows !=0 and rows != len(board) - 1):
        startCol = cols;
    #most bottom row
    elif (rows == len(board)-1 and cols != 0 and cols != len(board[0]) - 1):
        endRow = rows;
    #most right cols
    elif (cols == len(board[0]) - 1 and rows != 0 and rows !=len(board) - 1):
        endCol = cols;
    else:
        startCol = cols - 1
        endCol = cols + 1
        startRow = rows - 1
        endRow = rows + 1
    #non edge cases
    for row in board[startRow:endRow + 1]:
        for cell in row[startCol:endCol + 1]:
            if cell == "X":
                sum += 1;
    return sum

# precond: given a board and a cell
# postcond: return next generation cell state based on CGOL rules
# (alive 'X', dead ' ')
def get_next_gen_cell(board, rows, cols):
    numNeighbors = count_neighbours(board, rows, cols)
    newCell = ' '
    if (board[rows][cols] == 'X'):
        if (numNeighbors > 3 or numNeighbors < 2):
            newCell = ' ' # cell dies
        else:
            newCell = 'X' # cell lives
    else:
        if numNeighbors == 3:
            newCell = 'X' # cell is born
        else:
            newCell = ' ' # cell stays dead
    return newCell

# generate new board representing next generation
def generate_next_board(board):
    nextBoard=create_new_board(len(board),len(board[0]));
    r = 0;
    c = 0;
    while r < len(board):
        while c < len(board[0]):
            nextBoard[r][c] = get_next_gen_cell(board,r,c)
            c += 1
        r += 1;
    return nextBoard;

# pause for n milliseconds

# "repaint" by using an ANSI control character to
# repeatedly place the cursor at the origin (upper left)

# main function (written with python if name idiom)
if __name__ == '__main__':
    board1 = create_new_board(30, 30)
    # print_board(board1)
    set_cell(board1, 0, 0, 'X')
    set_cell(board1, 0, 1, 'X')
    set_cell(board1, 0, 5, 'X')
    set_cell(board1, 10, 5, 'X')
    set_cell(board1, 15, 20, 'X')
    set_cell(board1, 29, 29, 'X')
    print_board(board1)
    print("------------------")
    print_board(generate_next_board(board1))
