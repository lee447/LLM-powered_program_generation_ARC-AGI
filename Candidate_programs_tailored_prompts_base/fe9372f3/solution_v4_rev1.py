from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    r0 = c0 = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2 and 0 <= r-1 < h and 0 <= r+1 < h and 0 <= c-1 < w and 0 <= c+1 < w:
                if grid[r-1][c] == 2 and grid[r+1][c] == 2 and grid[r][c-1] == 2 and grid[r][c+1] == 2:
                    r0, c0 = r, c
                    break
        if r0 is not None:
            break
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2:
                out[r][c] = 2
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for dr, dc in dirs:
        step = 1
        while True:
            nr, nc = r0 + dr*step, c0 + dc*step
            if not (0 <= nr < h and 0 <= nc < w):
                break
            if grid[nr][nc] == 2:
                out[nr][nc] = 2
            else:
                if abs(dr) + abs(dc) == 1:
                    if step >= 2:
                        out[nr][nc] = 8 if (step-2) % 3 < 2 else 4
                    else:
                        out[nr][nc] = 8
                else:
                    out[nr][nc] = 1
            step += 1
    return out