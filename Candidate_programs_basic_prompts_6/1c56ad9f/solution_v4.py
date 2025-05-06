from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    out = [[0]*C for _ in range(R)]
    cols = sorted({c for r in range(R) for c in range(C) if sum(grid[i][c]>0 for i in range(R))>1})
    rows = sorted({r for r in range(R) for c in range(C) if sum(grid[r][j]>0 for j in range(C))>1})
    def blocks(lines):
        return [(lines[i], lines[i+1]) for i in range(len(lines)-1)]
    for r0,r1 in blocks(rows):
        H = r1 - r0
        for c0,c1 in blocks(cols):
            W = c1 - c0
            cells = []
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if grid[r][c]:
                        cells.append((r-r0, c-c0, grid[r][c]))
            for dr, dc, v in cells:
                nr, nc = dc, H - dr
                out[r0+nr][c0+nc] = v
    return out