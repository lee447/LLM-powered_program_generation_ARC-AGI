from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [[0]*W for _ in range(H)]
    positions = [(r,c) for r in range(H) for c in range(W) if grid[r][c]!=0]
    if not positions:
        return grid
    color = grid[positions[0][0]][positions[0][1]]
    coords = [(r,c) for r,c in positions if grid[r][c]==color]
    rows = sorted({r for r,c in coords})
    cols = sorted({c for r,c in coords})
    full = []
    for r in rows:
        for c in range(W-1):
            if grid[r][c]==color and grid[r][c+1]==color:
                full.append(r)
                break
    full = sorted(full)
    cycle = [-1,0,1,0]
    for r,c in coords:
        if r in full:
            out[r][c] = color
        else:
            idx = 0
            for a,b in zip(full, full[1:]):
                if a<r<b:
                    idx = r - a - 1
                    break
            off = cycle[idx % 4]
            nc = c + off
            if 0 <= nc < W:
                out[r][nc] = color
    return out