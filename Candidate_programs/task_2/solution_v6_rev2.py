from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    coords = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 8]
    if not coords:
        return []
    ys = [i for i, _ in coords]
    xs = [j for _, j in coords]
    ymin, ymax = min(ys), max(ys)
    xmin, xmax = min(xs), max(xs)
    h, w = ymax - ymin + 1, xmax - xmin + 1
    orig_top = grid[ymin - 1][xmin : xmax + 1] if ymin > 0 else None
    orig_bottom = grid[ymax + 1][xmin : xmax + 1] if ymax + 1 < H else None
    orig_left = [grid[y][xmin - 1] for y in range(ymin, ymax + 1)] if xmin > 0 else None
    orig_right = [grid[y][xmax + 1] for y in range(ymin, ymax + 1)] if xmax + 1 < W else None
    for r0 in range(H - h + 1):
        for c0 in range(W - w + 1):
            if r0 == ymin and c0 == xmin:
                continue
            bad = False
            for i in range(h):
                for j in range(w):
                    if grid[r0 + i][c0 + j] == 8:
                        bad = True
                        break
                if bad:
                    break
            if bad:
                continue
            if orig_top is None:
                if r0 != 0:
                    continue
            else:
                if r0 - 1 < 0 or grid[r0 - 1][c0 : c0 + w] != orig_top:
                    continue
            if orig_bottom is None:
                if r0 + h != H:
                    continue
            else:
                if r0 + h >= H or grid[r0 + h][c0 : c0 + w] != orig_bottom:
                    continue
            if orig_left is None:
                if c0 != 0:
                    continue
            else:
                if c0 - 1 < 0 or [grid[r0 + i][c0 - 1] for i in range(h)] != orig_left:
                    continue
            if orig_right is None:
                if c0 + w != W:
                    continue
            else:
                if c0 + w >= W or [grid[r0 + i][c0 + w] for i in range(h)] != orig_right:
                    continue
            return [grid[r0 + i][c0 : c0 + w] for i in range(h)]
    return []