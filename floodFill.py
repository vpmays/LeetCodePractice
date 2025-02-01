def floodFill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    visited = []
    queue = []
    start = [sr,sc]
    queue.append(start)
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    rows = len(image)
    columns = len(image[0])

    while queue:
        currentNode = queue.pop(0)
        if currentNode not in visited:
            for dir in dirs:
                nextNode = list(currentNode)
                nextNode[0] += dir[0]
                nextNode[1] += dir[1]
                if (0 <= nextNode[0] < rows) and (0 <= nextNode[1] < columns):
                    if image[nextNode[0]][nextNode[1]] == image[currentNode[0]][currentNode[1]]:
                        queue.append(nextNode)
            image[currentNode[0]][currentNode[1]] = color
            visited.append(currentNode)
    return image
image1 = [[1,1,1],
          [1,1,0],
          [1,0,1]
          ]
sr1 = 1
sc1 = 1
color1 = 2

print(floodFill(image1, sr1, sc1, color1))