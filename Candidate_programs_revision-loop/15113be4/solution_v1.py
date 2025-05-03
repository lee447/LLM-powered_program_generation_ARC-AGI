def solve(grid):
    H, W = len(grid), len(grid[0])
    divs = [i for i in range(H) if all(grid[i][j] == 4 for j in range(W))]
    bounds = [-1] + divs + [H]
    for b in range(len(bounds) - 1):
        top, bottom = bounds[b] + 1, bounds[b + 1] - 1
        if top > bottom:
            continue
        seed = []
        val = None
        for r in range(top, bottom + 1):
            for c in range(W):
                v = grid[r][c]
                if v not in (0, 1, 4):
                    val = v
                    seed.append((r, c))
        if not seed:
            continue
        cnt = len(seed)
        sr = sum(r for r, _ in seed) / cnt
        sc = sum(c for _, c in seed) / cnt
        rels = [(r - sr, c - sc) for r, c in seed]
        seen = [[False] * W for _ in range(H)]
        for r in range(top, bottom + 1):
            for c in range(W):
                if grid[r][c] == 1 and not seen[r][c]:
                    stack = [(r, c)]
                    seen[r][c] = True
                    cluster = []
                    while stack:
                        pr, pc = stack.pop()
                        cluster.append((pr, pc))
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = pr + dr, pc + dc
                            if top <= nr <= bottom and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc] == 1:
                                seen[nr][nc] = True
                                stack.append((nr, nc))
                    if len(cluster) != cnt:
                        continue
                    cr = sum(r for r, _ in cluster) / cnt
                    cc = sum(c for _, c in cluster) / cnt
                    mp = {}
                    for pr, pc in cluster:
                        key = (round(pr - cr, 3), round(pc - cc, 3))
                        mp[key] = (pr, pc)
                    for dr, dc in rels:
                        key = (round(dr, 3), round(dc, 3))
                        if key in mp:
                            rr, cc0 = mp[key]
                            grid[rr][cc0] = val
    return grid