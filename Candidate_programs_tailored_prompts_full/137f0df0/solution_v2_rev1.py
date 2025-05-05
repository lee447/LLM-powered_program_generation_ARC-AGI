from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    anchors = []
    for r in range(H-1):
        for c in range(W-1):
            v = grid[r][c]
            if v != 0 and grid[r+1][c] == v and grid[r][c+1] == v and grid[r+1][c+1] == v:
                anchors.append((r, c))
    if not anchors:
        return grid
    anchors.sort()
    rows = sorted({r for r, _ in anchors})
    cols = sorted({c for _, c in anchors})
    ar, ac = anchors[0]
    v0 = grid[ar][ac]
    N = 1
    while ar+N < H and ac+N < W and all(grid[ar+i][ac+j] == v0 for i in range(N+1) for j in range(N+1)):
        N += 1
    row_gaps = [(rows[i] + N, rows[i+1] - rows[i] - N) for i in range(len(rows)-1) if rows[i+1] - rows[i] - N > 0]
    col_gaps = [(cols[i] + N, cols[i+1] - cols[i] - N) for i in range(len(cols)-1) if cols[i+1] - cols[i] - N > 0]
    leftcap = cols[0]
    rightcap = W - (cols[-1] + N)
    topcap = rows[0]
    bottomcap = H - (rows[-1] + N)
    res = [row[:] for row in grid]
    for r0, rsz in row_gaps:
        for r in range(r0, r0 + rsz):
            for c in range(W):
                if grid[r][c] == 0:
                    res[r][c] = 2
    for c0, csz in col_gaps:
        for c in range(c0, c0 + csz):
            for r in range(H):
                if grid[r][c] == 0:
                    res[r][c] = 2
    for r0, rsz in row_gaps:
        for r in range(r0, r0 + rsz):
            for c in range(leftcap):
                res[r][c] = 1
            for c in range(W - rightcap, W):
                res[r][c] = 1
    for c0, csz in col_gaps:
        for c in range(c0, c0 + csz):
            for r in range(topcap):
                res[r][c] = 1
            for r in range(H - bottomcap, H):
                res[r][c] = 1
    return res