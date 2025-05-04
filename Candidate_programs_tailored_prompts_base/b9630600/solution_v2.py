def solve(grid):
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    rects = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 3 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == 3:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                min_i = min(x for x, y in cells)
                max_i = max(x for x, y in cells)
                min_j = min(y for x, y in cells)
                max_j = max(y for x, y in cells)
                rects.append((min_i, max_i, min_j, max_j))
    mid_r, mid_c = R/2, C/2
    TL = TR = BL = BR = None
    for min_i, max_i, min_j, max_j in rects:
        ci = (min_i + max_i) / 2
        cj = (min_j + max_j) / 2
        if ci < mid_r:
            if cj < mid_c:
                TL = (min_i, max_i, min_j, max_j)
            else:
                TR = (min_i, max_i, min_j, max_j)
        else:
            if cj < mid_c:
                BL = (min_i, max_i, min_j, max_j)
            else:
                BR = (min_i, max_i, min_j, max_j)
    out = [row[:] for row in grid]
    # horizontal links
    for A, B in ((TL, TR), (BL, BR)):
        mi = (A[0] + A[1]) // 2
        start = A[3]
        end = B[2]
        for j in range(start, end+1):
            out[mi][j] = 3
    # vertical links
    for A, B in ((TL, BL), (TR, BR)):
        mj = (A[2] + A[3]) // 2
        start = A[1]
        end = B[0]
        for i in range(start, end+1):
            out[i][mj] = 3
    return out