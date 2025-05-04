def solve(grid):
    from collections import Counter
    h, w = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg, _ = cnt.most_common(1)[0]
    rows = [i for i in range(h) if len({grid[i][j] for j in range(w)})==1]
    cols = [j for j in range(w) if len({grid[i][j] for i in range(h)})==1]
    rows.sort(); cols.sort()
    r0, r1 = rows[0], rows[1]
    c0, c1 = cols[0], cols[1]
    interior = [row[c0+1:c1] for row in grid[r0+1:r1]]
    stripe = grid[r0][0]
    if stripe == bg:
        colors = Counter(c for row in interior for c in row)
        fill = colors.most_common(1)[0][0]
        return [[fill]*len(interior[0]) for _ in interior]
    return interior