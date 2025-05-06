def solve(grid):
    H, W = len(grid), len(grid[0])
    counts = {}
    for r in range(H):
        for c in range(W):
            counts[grid[r][c]] = counts.get(grid[r][c], 0) + 1
    best_color, best_area = None, 0
    for color, cnt in counts.items():
        if cnt < 4: continue
        r0, c0, r1, c1 = H, W, -1, -1
        for r in range(H):
            for c in range(W):
                if grid[r][c] == color:
                    r0, c0 = min(r0, r), min(c0, c)
                    r1, c1 = max(r1, r), max(c1, c)
        h, w = r1 - r0 + 1, c1 - c0 + 1
        if h * w == cnt and h >= 2 and w >= 2 and h * w > best_area:
            best_area = h * w
            best_color = color
            br0, bc0, bh, bw = r0, c0, h, w
    r0, c0, h, w = br0, bc0, bh, bw
    if h < w:
        out = []
        for dr in range(h - 1):
            out.append(grid[r0 + dr + 1][c0 : c0 + w])
        return out
    else:
        out = []
        for dr in range(h):
            out.append(grid[r0 + dr][c0 + 1 : c0 + w])
        return out