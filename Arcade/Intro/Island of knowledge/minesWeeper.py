""""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
                       
""""

def find_num_mines_around(matrix, row, col):
    try:
        if row < 0 or row > len(matrix):
            return 0
        if col > len(matrix[0]) or col < 0:
            return 0
        if matrix[row][col] is True:
            return 1
    except IndexError:
        return 0
    return 0


def count_mine_around(matrix, row, col):
    top_r = find_num_mines_around(matrix, row-1, col+1)
    top = find_num_mines_around(matrix, row-1, col)
    top_l = find_num_mines_around(matrix, row-1, col-1)
    r = find_num_mines_around(matrix, row, col+1)
    bot_r = find_num_mines_around(matrix, row+1, col+1)
    bot = find_num_mines_around(matrix, row+1, col)
    bot_l = find_num_mines_around(matrix, row+1, col-1)
    l = find_num_mines_around(matrix, row, col-1)
    sum = top_r + top + top_l + r + bot_r + bot + bot_l + l
    print("sum:", sum)
    return sum


def minesweeper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    res = []
    for i in range(0, row):
        temp = []
        for j in range(0, col):
            temp.append(count_mine_around(matrix, i, j))
        res.append(temp)
    return res

    
