def solve(grid):
    h = len(grid)
    w = len(grid[0])
    row_bg = []
    for r in range(h):
        cnt = {}
        for c in grid[r]:
            cnt[c] = cnt.get(c, 0) + 1
        bg = max(cnt, key=lambda x: cnt[x])
        row_bg.append(bg)
    panels = []
    segs = []
    start = 0
    for i in range(1, h + 1):
        if i == h or row_bg[i] != row_bg[start]:
            segs.append((start, i - 1, row_bg[start]))
            start = i
    if len(segs) > 1:
        for r0, r1, bg in segs:
            panels.append((r0, r1, 0, w - 1, bg))
    else:
        col_bg = []
        for c in range(w):
            cnt = {}
            for r in range(h):
                cnt[grid[r][c]] = cnt.get(grid[r][c], 0) + 1
            bg = max(cnt, key=lambda x: cnt[x])
            col_bg.append(bg)
        segs = []
        start = 0
        for j in range(1, w + 1):
            if j == w or col_bg[j] != col_bg[start]:
                segs.append((start, j - 1, col_bg[start]))
                start = j
        for c0, c1, bg in segs:
            panels.append((0, h - 1, c0, c1, bg))
    bgs = sorted({p[4] for p in panels})
    small = bgs[0] if len(bgs) > 1 else bgs[0]
    comps = []
    for r0, r1, c0, c1, bg in panels:
        vis = [[False] * w for _ in range(h)]
        for r in range(r0, r1 + 1):
            for c in range(c0, c1 + 1):
                if not vis[r][c] and grid[r][c] != bg:
                    color = grid[r][c]
                    stack = [(r, c)]
                    vis[r][c] = True
                    pixels = []
                    min_r = r1
                    max_r = r0
                    min_c = c1
                    max_c = c0
                    while stack:
                        y, x = stack.pop()
                        pixels.append((y, x))
                        if y < min_r: min_r = y
                        if y > max_r: max_r = y
                        if x < min_c: min_c = x
                        if x > max_c: max_c = x
                        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            ny, nx = y + dy, x + dx
                            if r0 <= ny <= r1 and c0 <= nx <= c1 and not vis[ny][nx] and grid[ny][nx] == color:
                                vis[ny][nx] = True
                                stack.append((ny, nx))
                    comps.append((pixels, min_r, max_r, min_c, max_c, color, r0, r1, c0, c1, bg))
    out = [row[:] for row in grid]
    for pixels, _, _, _, _, _, _, _, _, _, bg in comps:
        for y, x in pixels:
            out[y][x] = bg
    for pixels, _, _, min_c, max_c, color, r0, r1, c0, c1, bg in comps:
        width = max_c - min_c + 1
        if bg == small:
            dest_min = c1 - width + 1
        else:
            dest_min = c0
        delta = dest_min - min_c
        for y, x in pixels:
            out[y][x + delta] = color
    return out