from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    rects = []
    for r in range(H-1):
        for c in range(W-1):
            if orig[r][c] == 1 and (r == 0 or orig[r-1][c] != 1) and (c == 0 or orig[r][c-1] != 1) and orig[r][c+1] == 1 and orig[r+1][c] == 1:
                c2 = c
                while c2+1 < W and orig[r][c2+1] == 1:
                    c2 += 1
                r2 = r
                while r2+1 < H and orig[r2+1][c] == 1:
                    r2 += 1
                if r2 <= r+1 or c2 <= c+1:
                    continue
                ok = True
                for x in range(c, c2+1):
                    if orig[r][x] != 1 or orig[r2][x] != 1:
                        ok = False
                        break
                if not ok:
                    continue
                for y in range(r, r2+1):
                    if orig[y][c] != 1 or orig[y][c2] != 1:
                        ok = False
                        break
                if not ok:
                    continue
                colors = set()
                for i in range(r+1, r2):
                    for j in range(c+1, c2):
                        v = orig[i][j]
                        if v != 0 and v != 1:
                            colors.add(v)
                if not colors:
                    continue
                color = colors.pop()
                rects.append((r, r2, c, c2, color))
    out = [row[:] for row in orig]
    for r, r2, c, c2, color in rects:
        for i in range(r+1, r2):
            for j in range(c+1, c2):
                if out[i][j] == 1:
                    out[i][j] = color
    return out