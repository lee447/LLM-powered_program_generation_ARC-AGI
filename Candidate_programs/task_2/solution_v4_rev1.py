from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    coords = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 8]
    ys = [i for i, _ in coords]
    xs = [j for _, j in coords]
    ymin, ymax = min(ys), max(ys)
    xmin, xmax = min(xs), max(xs)
    h, w = ymax - ymin + 1, xmax - xmin + 1
    top = grid[ymin - 1][xmin : xmax + 1] if ymin > 0 else None
    bottom = grid[ymax + 1][xmin : xmax + 1] if ymax + 1 < H else None
    left = [grid[y][xmin - 1] for y in range(ymin, ymax + 1)] if xmin > 0 else None
    right = [grid[y][xmax + 1] for y in range(ymin, ymax + 1)] if xmax + 1 < W else None
    for r0 in range(H - h + 1):
        for c0 in range(W - w + 1):
            if not (r0 + h - 1 < ymin or r0 > ymax or c0 + w - 1 < xmin or c0 > xmax):
                continue
            ok = True
            for i in range(h):
                for j in range(w):
                    if grid[r0 + i][c0 + j] == 8:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            if top is not None and grid[r0 - 1][c0 : c0 + w] != top:
                continue
            if bottom is not None and grid[r0 + h][c0 : c0 + w] != bottom:
                continue
            if left is not None and [grid[r0 + i][c0 - 1] for i in range(h)] != left:
                continue
            if right is not None and [grid[r0 + i][c0 + w] for i in range(h)] != right:
                continue
            return [grid[r0 + i][c0 : c0 + w] for i in range(h)]
    return []