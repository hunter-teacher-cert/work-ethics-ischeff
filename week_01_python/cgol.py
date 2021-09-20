# initialize empty board (all cells dead)

# print the board to the terminal

# set a single cell  located at (rows, cols) to value val

# return number of living neigbours of board[r][c]


# precond: given a board and a cell
# postcond: return next generation cell state based on CGOL rules
# (alive 'X', dead ' ')

# generate new board representing next generation

# pause for n milliseconds

# "repaint" by using an ANSI control character to
# repeatedly place the cursor at the origin (upper left)


def print_board(width, length):
    for i in range(width):
        for j in range(length):
            print
