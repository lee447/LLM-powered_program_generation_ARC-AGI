def solve(grid):
    n, m = len(grid), len(grid[0])
    # find the marker color (8 if present, else the smallest non-background)
    from collections import Counter
    cnt = Counter()
    for r in grid:
        cnt.update(r)
    marker = 8 if cnt[8] > 0 else sorted([c for c, v in cnt.items() if c not in (0, 9)], reverse=True)[0]
    # bounding box of marker
    r0, c0 = n, m
    r1 = c1 = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == marker:
                r0 = min(r0, i); c0 = min(c0, j)
                r1 = max(r1, i); c1 = max(c1, j)
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    # try extract above
    if r0 >= h:
        above = [row[c0:c1+1] for row in grid[r0-h:r0]]
        if all(marker not in row for row in above):
            return above
    # try left
    if c0 >= w:
        left = [row[c0-w:c0] for row in grid[r0:r1+1]]
        if all(marker not in row for row in left):
            return left
    # try below
    if r1 + h < n:
        below = [row[c0:c1+1] for row in grid[r1+1:r1+1+h]]
        if all(marker not in row for row in below):
            return below
    # try right
    if c1 + w < m:
        right = [row[c1+1:c1+1+w] for row in grid[r0:r1+1]]
        if all(marker not in row for row in right):
            return right
    return []