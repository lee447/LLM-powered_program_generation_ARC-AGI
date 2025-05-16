from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = Counter(val for row in grid for val in row)
    bg = cnt.most_common(1)[0][0]
    S = None
    blocks = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == bg: continue
            # possible border-top
            for size in range(3, min(h - r, w - c) + 1):
                if all(grid[r][c + j] == grid[r][c] for j in range(size)) and \
                   all(grid[r + size - 1][c + j] == grid[r][c] for j in range(size)) and \
                   all(grid[r + i][c] == grid[r][c] for i in range(size)) and \
                   all(grid[r + i][c + size - 1] == grid[r][c] for i in range(size)):
                    if size > 2:
                        f = grid[r + 1][c + 1]
                        if f != grid[r][c] and all(grid[r + i][c + j] == f for i in range(1, size - 1) for j in range(1, size - 1)):
                            blocks.append((r, c, size, grid[r][c], f))
                            S = size
                    break
    if not blocks:
        return grid
    rows = sorted({r for r, _, _, _, _ in blocks})
    cols = sorted({c for _, c, _, _, _ in blocks})
    rmap = {r: i for i, r in enumerate(rows)}
    cmap = {c: j for j, c in enumerate(cols)}
    R, C = len(rows), len(cols)
    out = [[bg] * w for _ in range(h)]
    for r0, c0, size, bcol, fcol in blocks:
        i, j = rmap[r0], cmap[c0]
        nr, nc = i * size, j * size
        for di in range(size):
            for dj in range(size):
                out[nr + di][nc + dj] = bcol if di in (0, size - 1) or dj in (0, size - 1) else fcol
    return out