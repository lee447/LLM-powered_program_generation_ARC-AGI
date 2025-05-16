def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    from collections import Counter
    # find plus color as the one forming a cross
    cnt = Counter(c for row in grid for c in row if c != border)
    # border and background are most common; plus is next common distinct segment
    bg, plus = cnt.most_common()[:2]
    bg = bg[0]
    plus = plus[0]
    # hole color is the remaining non-border, non-bg, non-plus
    colors = set(cnt) - {border, bg, plus}
    hole = colors.pop() if colors else None
    # find center of plus
    rows = [r for r in range(h) for c in range(w) if grid[r][c] == plus]
    cols = [c for r in range(h) for c in range(w) if grid[r][c] == plus]
    cr = sum(rows) // len(rows)
    cc = sum(cols) // len(cols)
    # collect hole positions
    holes = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == hole]
    # detect main diagonal (r,c) with most freq of c-r
    drs = Counter(c - r for r, c in holes)
    main_dr, _ = drs.most_common(1)[0]
    # reflect main-diagonal holes across vertical axis
    for r, c in holes:
        if c - r == main_dr:
            cs = 2 * cc - c
            if 0 <= cs < w and grid[r][cs] != border and grid[r][cs] != plus:
                grid[r][cs] = hole
    return grid