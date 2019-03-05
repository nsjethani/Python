def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    no_of_island = 0
    nr = len(grid)
    nc = len(grid[0])
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "1":
                no_of_island += 1
                q = []
                q.append((i, j))
                print(q)
                while q:
                    print(q)
                    x = q.pop()
                    r,c=x[0],x[1]
                    grid[r][c] = 0
                    if r - 1 >= 0 and grid[r - 1][c]=="1":
                        q.append((r - 1, c))
                        grid[r - 1][c] = 0
                    if c + 1 < nc and grid[r][c + 1]=="1":
                        q.append((r, c + 1))
                        grid[r][c + 1] = 0
                    if r + 1 < nr and grid[r + 1][c]=="1":
                        q.append((r + 1, c))
                        grid[r + 1][c] = 0
                    if r - 1 >= 0 and grid[r-1][c]=="1":
                        q.append((r, c - 1))
                        grid[r][c - 1] = 0
    return no_of_island

ans = numIslands([["1","1","0","0","0"],
                  ["1","1","0","0","0"],
                  ["0","0","1","0","0"],
                  ["0","0","0","1","1"]])
print(ans)