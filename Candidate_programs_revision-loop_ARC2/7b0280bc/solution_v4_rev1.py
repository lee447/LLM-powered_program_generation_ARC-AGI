from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    changes = {}
    for i in range(h - 1):
        for j in range(w - 1):
            c = grid[i][j]
            if c != bg and grid[i][j+1] == c and grid[i+1][j] == c and grid[i+1][j+1] == c:
                changes.setdefault(c, []).append((i, j))
    out = [row[:] for row in grid]
    for c, pos in changes.items():
        k = len(pos)
        if k < 2:
            continue
        col = 5 if c % 2 == 0 else 3
        if k == 2:
            for i, j in pos:
                out[i][j] = out[i][j+1] = out[i+1][j] = out[i+1][j+1] = col
        else:
            if c % 2 == 0:
                if k % 2:
                    start = k//2 + 1
                else:
                    start = k//2
                for i, j in pos[start:]:
                    out[i][j] = out[i][j+1] = out[i+1][j] = out[i+1][j+1] = col
            else:
                if k % 2:
                    end = k//2
                else:
                    end = k//2 - 1
                for i, j in pos[:end]:
                    out[i][j] = out[i][j+1] = out[i+1][j] = out[i+1][j+1] = col
    return out