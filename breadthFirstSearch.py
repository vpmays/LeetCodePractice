visited = []
queue = []

def bfs(graph, start):

    queue.append(start)

    while queue:
        currentNode = queue.pop(0)
        if currentNode not in visited:
            for neighbor in graph[currentNode]:
                queue.append(neighbor)
            visited.append(currentNode)
        else:
            print(f"Already visited: {currentNode}")

graph1 = {
    '5' : ['7','10','1'],
    '7' : ['3'],
    '10' : ['3','2'],
    '1' : ['2'],
    '3' : ['2'],
    '2' : []
}

graph2 = {
    '5' : ['7','10','1'],
    '7' : ['3', '5'],
    '10' : ['3','2', '5'],
    '1' : ['2', '5'],
    '3' : ['2', '10', '7'],
    '2' : ['3','10','1']
}

bfs(graph1, '5')
print(visited)
