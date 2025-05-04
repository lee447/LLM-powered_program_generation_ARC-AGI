def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    pairs = []
    used = set()
    for r in range(h):
        for c in range(w):
            for dr, dc in [(0,1),(1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < h and 0 <= nc < w:
                    a, b = grid[r][c], grid[nr][nc]
                    if a != 0 and b != 0 and a != b:
                        key = tuple(sorted(((r,c),(nr,nc))))
                        if key in used: continue
                        ok = True
                        for rr, cc in [(r,c),(nr,nc)]:
                            col = grid[rr][cc]
                            for ddr, ddc in dirs:
                                ir, ic = rr+ddr, cc+ddc
                                if (ir, ic) != (r,c) and (ir, ic) != (nr,nc):
                                    if 0 <= ir < h and 0 <= ic < w and grid[ir][ic] == col:
                                        ok = False; break
                            if not ok: break
                        if ok:
                            pairs.append(((r,c),(nr,nc)))
                            used.add(key)
    anchor_pos = set()
    for a,b in pairs:
        anchor_pos.add(a); anchor_pos.add(b)
    rem = [(r,c) for r in range(h) for c in range(w) if grid[r][c] != 0 and (r,c) not in anchor_pos]
    minr = min(r for r,c in rem)
    maxr = max(r for r,c in rem)
    minc = min(c for r,c in rem)
    maxc = max(c for r,c in rem)
    sub = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
    in_colors = set(x for row in sub for x in row)
    mapping = {}
    for (r1,c1),(r2,c2) in pairs:
        x, y = grid[r1][c1], grid[r2][c2]
        if x in in_colors:
            mapping[x] = y
        if y in in_colors:
            mapping[y] = x
    out = []
    for r in range(minr, maxr+1):
        row = []
        for c in range(minc, maxc+1):
            v = grid[r][c]
            row.append(mapping.get(v, v))
        out.append(row)
    return out