from collections import Counter

def solve(grid):
    H, W = len(grid), len(grid[0])
    is_blank = [all(c == 0 for c in row) for row in grid]
    runs = []
    r = 0
    while r < H:
        if not is_blank[r]:
            start = r
            while r < H and not is_blank[r]:
                r += 1
            runs.append((start, r - start))
        else:
            r += 1
    if not runs:
        return grid
    lengths = [l for _, l in runs]
    L = Counter(lengths).most_common(1)[0][0]
    runs_L = [s for s, l in runs if l == L]
    canon_start = min(runs_L)
    res = [[0] * W for _ in range(H)]
    for s in runs_L:
        for i in range(L):
            res[s + i] = grid[canon_start + i].copy()
    return res