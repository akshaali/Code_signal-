def matrixElementsSum(matrix):
    sum = 0
    for i in range(int(len(matrix[0]))):
        for j in range(int(len(matrix))):
            if matrix[j][i] == 0 :
                break
            else:
                sum += matrix[j][i]
    return sum
