def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    
    print(matrix)
    rows = []
    columns = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 0:
                rows.append(row)
                columns.append(column)

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if row in rows:
                matrix[row][column] = 0
            elif column in columns:
                matrix[row][column] = 0
                
    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))