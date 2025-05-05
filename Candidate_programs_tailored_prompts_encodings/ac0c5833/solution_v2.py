def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    cluster = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 2]
    anchor_set = set(anchors)
    for ar, ac in anchors:
        offsets = [(r - ar, c - ac) for r, c in cluster]
        ok = True
        for br, bc in anchors:
            for dr, dc in offsets:
                rr, cc = br + dr, bc + dc
                if not (0 <= rr < H and 0 <= cc < W) or (rr, cc) in anchor_set:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            chosen = offsets
            break
    out = [[0]*W for _ in range(H)]
    for r, c in anchors:
        out[r][c] = 4
    for br, bc in anchors:
        for dr, dc in chosen:
            out[br+dr][bc+dc] = 2
    return out