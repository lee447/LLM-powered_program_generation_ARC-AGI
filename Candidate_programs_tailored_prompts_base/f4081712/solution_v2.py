def solve(grid):
    n, m = len(grid), len(grid[0])
    from collections import Counter
    # identify background color (most common on the perimeter)
    border = [grid[i][0] for i in range(n)] + [grid[i][m-1] for i in range(n)] + \
             [grid[0][j] for j in range(m)] + [grid[n-1][j] for j in range(m)]
    bg = Counter(border).most_common(1)[0][0]
    # find the largest solid rectangle of a single non-background color
    best = (0, 0, 0, 0, 0)  # area, top, left, height, width
    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            if c == bg:
                continue
            maxw = 0
            while j + maxw < m and grid[i][j + maxw] == c:
                maxw += 1
            w = maxw
            h = 1
            while i + h < n:
                row = grid[i + h]
                k = 0
                while k < w and row[j + k] == c:
                    k += 1
                if k < w:
                    break
                h += 1
                w = k
            area = h * w
            if area > best[0]:
                best = (area, i, j, h, w)
    _, bi, bj, bh, bw = best
    # determine orientation and which corner-adjacent side
    horizontal = bw > bh
    # choose which corner side to extract from
    ci = 0 if bi < n//2 else n - bh
    cj = 0 if bj < m//2 else m - bw
    if horizontal:
        # band runs left-right, extract at (bi, cj) if top or bottom
        si = bi
        sj = cj if bj < m//2 else bj + bw - bw
    else:
        # band runs top-bottom, extract at (ci, bj)
        si = ci if bi < n//2 else bi + bh - bh
        sj = bj
    h, w = bh, bw
    return [row[sj:sj+w] for row in grid[si:si+h]]