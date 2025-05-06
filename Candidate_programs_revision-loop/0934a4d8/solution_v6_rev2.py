from collections import defaultdict
def solve(grid):
    H, W = len(grid), len(grid[0])
    eights = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 8]
    if not eights:
        return []
    rows = [i for i, _ in eights]
    cols = [j for _, j in eights]
    minr, maxr = min(rows), max(rows)
    minc, maxc = min(cols), max(cols)
    h, w = maxr - minr + 1, maxc - minc + 1
    counts = defaultdict(list)
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            ok = True
            for ii in range(i, i + h):
                for jj in range(j, j + w):
                    if grid[ii][jj] == 8:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            key = tuple(tuple(grid[ii][jj] for jj in range(j, j + w)) for ii in range(i, i + h))
            counts[key].append((i, j))
    if not counts:
        return []
    bestc = max(len(v) for v in counts.values())
    candidates = [k for k, v in counts.items() if len(v) == bestc]
    if len(candidates) == 1:
        best = candidates[0]
    else:
        best = min(candidates, key=lambda k: min(abs(i - minr) + abs(j - minc) for i, j in counts[k]))
    return [list(row) for row in best]