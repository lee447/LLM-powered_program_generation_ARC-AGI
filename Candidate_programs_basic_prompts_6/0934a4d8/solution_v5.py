def solve(grid):
    rows, cols = len(grid), len(grid[0])
    # find separator color (largest connected rectangle of one color)
    from collections import Counter
    cnt = Counter(c for row in grid for c in row if c is not None)
    sep = max(cnt, key=lambda c: (cnt[c] if c!=0 else -1))
    # locate sep rectangle
    minr, maxr = rows, -1
    minc, maxc = cols, -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == sep:
                minr = min(minr, i); maxr = max(maxr, i)
                minc = min(minc, j); maxc = max(maxc, j)
    h, w = maxr-minr+1, maxc-minc+1
    # extract rectangle of size h x w immediately above the sep block
    out = []
    for i in range(minr-h, minr):
        out.append(grid[i][minc:minc+w])
    return out