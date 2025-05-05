def solve(grid):
    H = len(grid)
    W = len(grid[0])
    row_anchors = [r for r in range(H) if all(grid[r][c]==0 for c in range(W))]
    col_anchors = [c for c in range(W) if all(grid[r][c]==0 for r in range(H))]
    out = [row[:] for row in grid]
    for i in range(len(row_anchors)-1):
        r0 = row_anchors[i] + 1
        r1 = row_anchors[i+1]
        for j in range(len(col_anchors)-1):
            c0 = col_anchors[j] + 1
            c1 = col_anchors[j+1]
            size = r1 - r0
            block = [[grid[r0+dr][c0+dc] for dc in range(size)] for dr in range(size)]
            for dr in range(size):
                for dc in range(size):
                    out[r0+dr][c0+dc] = block[size-1-dc][dr]
    return out