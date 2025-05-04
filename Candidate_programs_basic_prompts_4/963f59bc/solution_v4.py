from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c:
                counts[c] = counts.get(c, 0) + 1
    cA = max((c for c in counts if counts[c] > 1), key=lambda c: counts[c])
    A_pos = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == cA]
    rmin = min(i for i, _ in A_pos)
    rmax = max(i for i, _ in A_pos)
    cmin = min(j for _, j in A_pos)
    cmax = max(j for _, j in A_pos)
    hA, wA = rmax - rmin + 1, cmax - cmin + 1
    A_rel = [(i - rmin, j - cmin) for i, j in A_pos]
    B_colors = [c for c in counts if counts[c] == 1]
    res = [row[:] for row in grid]
    for cB in B_colors:
        rB, cBcol = next((i, j) for i in range(h) for j in range(w) if grid[i][j] == cB)
        for flip in ('h', 'v'):
            done = False
            for ri, ci in A_rel:
                if flip == 'h':
                    fr0, fc0 = ri, wA - 1 - ci
                else:
                    fr0, fc0 = hA - 1 - ri, ci
                r0, c0 = rB - fr0, cBcol - fc0
                pos = []
                ok = True
                for ri2, ci2 in A_rel:
                    if flip == 'h':
                        fr, fc = ri2, wA - 1 - ci2
                    else:
                        fr, fc = hA - 1 - ri2, ci2
                    r, c = r0 + fr, c0 + fc
                    if not (0 <= r < h and 0 <= c < w and (grid[r][c] == 0 or grid[r][c] == cB)):
                        ok = False
                        break
                    pos.append((r, c))
                if ok:
                    for r, c in pos:
                        res[r][c] = cB
                    done = True
                    break
            if done:
                break
    return res