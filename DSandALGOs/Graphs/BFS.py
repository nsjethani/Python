def BFS(graph, s):
    q = []
    q.append(s)
    visited = [False for i in range(len(graph))]
    visited[s] = True
    while q:
        node = q.pop(0)
        neighbours = graph[node]
        print(node, end = " ")
        for i in range(len(neighbours)):
            if not visited[neighbours[i]]:
                q.append(neighbours[i])
                visited[neighbours[i]] = True

g = [[1,2],[0,3,4],[0,4],[1,5,4],[1,2,3],[3,4]]

BFS(g,0)