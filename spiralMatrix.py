def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    myMatrix = list(matrix)
    numOfRows = len(myMatrix)
    numOfColumns = len(myMatrix[0])
    rowsVisited = []
    columnsVisited = []
    visitedAllElements = False
    spiralElements = []
    
    while visitedAllElements == False:
        #forward row
        i = 0
        for element in myMatrix[int(len(rowsVisited)/2)]:
            if element != None:
                spiralElements.append(element)
                myMatrix[int(len(rowsVisited)/2)][i] = None
            i += 1
        rowsVisited.append(int(len(rowsVisited)/2))
        print(f"after forward row: {myMatrix}")
        
        # descnding column
        for row in myMatrix:
            if row[numOfColumns - 1 - (int(len(columnsVisited)/2))] != None:
                spiralElements.append(row[numOfColumns - 1 - (int(len(columnsVisited)/2))])
                row[numOfColumns - 1 - (int(len(columnsVisited)/2))] = None
        columnsVisited.append(numOfColumns - 1 - int((len(columnsVisited)/2)))
        print(f"decending column row: {myMatrix}")
        
        # reverse row
        j = numOfColumns - 1
        for element in myMatrix[len(myMatrix) - (int(len(rowsVisited)/2)) - 1][::-1]:
            if element != None:
                spiralElements.append(element)
                myMatrix[len(myMatrix) - (int(len(rowsVisited)/2)) - 1][j] = None
            j -= 1
        rowsVisited.append(len(myMatrix) - (int(len(rowsVisited)/2)) - 1)
        
        # ascending column
        for row in myMatrix[::-1]:
            if row[int(len(columnsVisited)/2)] != None:
                spiralElements.append(row[int(len(columnsVisited)/2)])
                row[int(len(columnsVisited)/2)] = None
        columnsVisited.append(numOfColumns - 1 - (int(len(columnsVisited)/2)))

        if (len(rowsVisited) >= numOfRows) or (len(columnsVisited) >= numOfColumns):
            visitedAllElements = True
    
    return spiralElements

print(spiralOrder([[1,2,3],[8,9,4],[7,6,5]]))