from collections import Counter

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    min_r, max_r, min_c, max_c = rows, -1, cols, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 8:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    h, w = max_r - min_r + 1, max_c - min_c + 1
    cnt = Counter()
    for r in range(rows - h + 1):
        for c in range(cols - w + 1):
            ok = True
            block = []
            for dr in range(h):
                row = grid[r + dr][c:c + w]
                if 8 in row:
                    ok = False
                    break
                block.append(tuple(row))
            if ok:
                cnt[tuple(block)] += 1
    pattern = cnt.most_common(1)[0][0]
    return [list(row) for row in pattern]