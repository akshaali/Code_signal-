"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
"""

def spiralNumbers(n):
    M = [[0 for x in range(n)] for _ in range(n)]
    
    forward = n
    down = n - 1
    backward = n - 1
    up = n - 2
    
    pos = [0,0]
    cnt = 1
    
    while True:

        for _ in range(forward):
            M[pos[0]][pos[1]] = cnt
            pos[1] += 1
            cnt += 1
        pos[1] -= 1
        if cnt >= (n*n): return M

        for _ in range(down):
            pos[0] += 1
            M[pos[0]][pos[1]] = cnt
            cnt += 1

        for _ in range(backward):
            pos[1] -= 1
            M[pos[0]][pos[1]] = cnt
            cnt += 1

        for _ in range(up):
            pos[0] -= 1
            M[pos[0]][pos[1]] = cnt
            cnt += 1
        pos[1] += 1
        
        forward -= 2
        down -= 2
        backward -= 2
        up -= 2
