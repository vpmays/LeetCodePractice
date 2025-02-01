def numIslands(grid):
  """
  :type grid: List[List[str]]
  :rtype: int
  """
  lands = []
  dirs = [[0,1],[0,-1],[1,0],[-1,0]]
  islands = []

  for rowIndex in range(0, len(grid)):
    for columnIndex in range(0, len(grid[0])):
      queue = []
      #check if node is "1", if not, do nothing
      if grid[rowIndex][columnIndex] == "1":
        if [rowIndex,columnIndex] not in lands:
          islands.append([rowIndex,columnIndex])
          queue.append([rowIndex,columnIndex])
      #breadth first search to find all neighbors
      while queue:
        currentNode = queue.pop(0)
        currentRowIndex = currentNode[0]
        currentColumnIndex = currentNode[1]
        #loop through right,left,up,down and see if land is adjacent, if so add the node to lands
        for dir in dirs:
          currentRowIndex = currentRowIndex + dir[0]
          currentColumnIndex = currentColumnIndex + dir[1]
          #make sure you're in bounds
          if (0<=currentRowIndex<len(grid)) and (0<=currentColumnIndex<len(grid[0])):
            #see if neighbor node is land, add it to lands if so
            if grid[currentRowIndex][currentColumnIndex] == "1":
              #make sure node is not already in lands
              if [currentRowIndex,currentColumnIndex] not in lands:
                lands.append([currentRowIndex,currentColumnIndex])
                queue.append([currentRowIndex,currentColumnIndex]) #come check this later
          #after checking a direction, return back to current node
          currentRowIndex = currentNode[0]
          currentColumnIndex = currentNode[1]


  return len(islands)
  

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid1))