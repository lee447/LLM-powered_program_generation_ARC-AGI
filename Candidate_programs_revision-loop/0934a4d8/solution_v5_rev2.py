from collections import Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [r for r in range(h) for c in range(w) if grid[r][c] == 8]
    cols = [c for r in range(h) for c in range(w) if grid[r][c] == 8]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    cnt = Counter()
    for r in range(h - H + 1):
        for c in range(w - W + 1):
            block = []
            skip = False
            for i in range(r, r + H):
                row = []
                for j in range(c, c + W):
                    if grid[i][j] == 8:
                        skip = True
                        break
                    row.append(grid[i][j])
                if skip:
                    break
                block.append(tuple(row))
            if not skip:
                cnt[tuple(block)] += 1
    tile = cnt.most_common(1)[0][0]
    return [list(row) for row in tile]