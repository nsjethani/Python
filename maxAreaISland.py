def maxAreaOfIsland(grid):
    seen = set()
    print("A : ",seen)

    def area(r, c):
        print("B ",r,c,seen)
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        print("C ", r, c, seen)
        print(" ")
        ar = 1 + area(r + 1, c) + area(r - 1, c) + area(r, c - 1) + area(r, c + 1)
        print("ar ",ar, r, c)
        return ar

    max = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            print("loop")
            print("r c",r,c)
            a = area(r,c)
            if max<a:
                max=a
    return max


result = maxAreaOfIsland(
               [[0, 1, 1, 0, 1],
                [1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 1, 1, 0, 1]])

print(result)