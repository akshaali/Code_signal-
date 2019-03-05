""""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.
For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.

""""


def chessBoardCellColor(cell1, cell2):
    cell1a, cell1b, cell2a, cell2b = ord(cell1[0]) - 64 , int(cell1[1]), ord(cell2[0]) - 64, int(cell2[1])
    if cell1a % 2 == 0 and cell1b % 2 == 0 or cell1a % 2 != 0 and cell1b %2 != 0:
        color1 = True
    else:
        color1 = False
    if cell2a % 2 == 0 and cell2b % 2 == 0 or cell2a % 2 != 0 and cell2b % 2 != 0 :
        color2 = True
    else:
        color2 = False
    if color1 == color2:
        return True 
    else:
        return False
        

