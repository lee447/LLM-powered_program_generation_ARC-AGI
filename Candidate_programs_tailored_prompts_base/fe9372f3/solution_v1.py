def solve(grid: list[list[int]]) -> list[list[int]]:
    H = len(grid)
    W = len(grid[0])
    cy = cx = None
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 2:
                if 0 <= y-1 < H and 0 <= y+1 < H and 0 <= x-1 < W and 0 <= x+1 < W:
                    if grid[y-1][x] == 2 and grid[y+1][x] == 2 and grid[y][x-1] == 2 and grid[y][x+1] == 2:
                        cy, cx = y, x
                        break
        if cy is not None:
            break
    out = [[0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 2:
                out[y][x] = 2
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        y, x = cy, cx
        while True:
            y += dy
            x += dx
            if not (0 <= y < H and 0 <= x < W):
                break
            if grid[y][x] == 2:
                continue
            if y == 0 or y == H-1 or x == 0 or x == W-1:
                out[y][x] = 4
            else:
                out[y][x] = 8
    for dy, dx in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        y, x = cy, cx
        while True:
            y += dy
            x += dx
            if not (0 <= y < H and 0 <= x < W):
                break
            out[y][x] = 1
    return out