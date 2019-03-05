from queue import Queue

def shortestPath(grid, s):
    m, n = len(grid), len(grid[0])
    path_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_level = 0
    reached_end = False
    visited = [[0 for i in range(n)] for j in range(m)]
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    next_nodes = Queue()
    next_nodes.put(s)
    visited[s[0]][s[1]] = True
    while not next_nodes.empty():
        next_node = next_nodes.get()
        print(next_node)
        if grid[next_node[0]][next_node[1]] == 'E':
            reached_end = True
            print("in while")
            break
        print(reached_end)
        for i in range(4):
            rr = next_node[0] + dr[i]
            cc = next_node[1] + dc[i]
            if rr < 0 or cc <0:
                continue
            if rr>=m or cc>=n:
                continue
            if visited[rr][cc]:
                continue
            if grid[rr][cc] == '#':
                continue
            next_nodes.put((rr,cc))
            visited[rr][cc] = True
            nodes_in_next_level += 1
            print(nodes_in_next_level)
        nodes_left_in_layer -= 1
        print("left",nodes_left_in_layer)
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_level
            nodes_in_next_level = 0
            path_count+=1
    if reached_end:
        return path_count
    return -1

grid = [['S', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '.', '.', '.'],
        ['#', '.', '#', 'E', '.', '#', '.'],
        ]

grid1 = [
    ['S', '#', '#'],
    ['.', '#', '#'],
    ['.', 'E', '.']
]

print(grid)
ret = shortestPath(grid1, (0,0))
print("aNSWER", ret)