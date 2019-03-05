def hasPath(maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """
    nr, nc = len(maze), len(maze[0])
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    qu = [start]
    visited[start[0]][start[1]] = True
    while qu:
        point = qu.pop(0)
        if point[0] == destination[0] and point[1] == destination[1]:
            return True
        x = point[0]
        y = point[1]

        for d in dirs:
            p = x + d[0]
            q = y + d[1]
            while p >= 0 and q >= 0 and p < nr and q < nc and maze[x][y] == 0:
                p += d[0]
                q += d[1]
            if not visited[p - d[0]][q - d[1]]:
                qu.append([p - d[0], q - d[1]])
                visited[p - d[0]][q - d[1]] = True
    return False

ans = hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [1,2])
print(ans)