def solve(grid):
    H = len(grid)
    W = len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                cells = []
                stack = [(i,j)]
                visited[i][j] = True
                min_r = max_r = i
                min_c = max_c = j
                while stack:
                    r,c = stack.pop()
                    v = grid[r][c]
                    cells.append((r,c,v))
                    if r < min_r: min_r = r
                    if r > max_r: max_r = r
                    if c < min_c: min_c = c
                    if c > max_c: max_c = c
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append({
                    'cells': cells,
                    'min_r': min_r, 'max_r': max_r,
                    'min_c': min_c, 'max_c': max_c,
                    'w': max_c-min_c+1,
                    'h': max_r-min_r+1
                })
    comps.sort(key=lambda x: x['min_r'])
    groups = []
    seeds = []
    for comp in comps:
        if not groups:
            groups.append([comp])
            seeds.append(comp)
        else:
            seed = seeds[-1]
            if comp['min_r'] <= seed['max_r'] and comp['max_r'] >= seed['min_r']:
                groups[-1].append(comp)
            else:
                groups.append([comp])
                seeds.append(comp)
    out = [[0]*W for _ in range(H)]
    placed = set()
    for group in groups:
        group.sort(key=lambda x: x['min_c'])
        widths = [c['w'] for c in group]
        total_w = sum(widths)
        start = W - total_w
        while True:
            offsets = []
            acc = 0
            for w in widths:
                offsets.append(start+acc)
                acc += w
            conflict = False
            for idx, comp in enumerate(group):
                off = offsets[idx]
                for r,c,v in comp['cells']:
                    nc = off + (c - comp['min_c'])
                    if (r,nc) in placed:
                        conflict = True
                        break
                if conflict:
                    break
            if conflict:
                start -= 1
            else:
                break
        for idx, comp in enumerate(group):
            off = offsets[idx]
            for r,c,v in comp['cells']:
                nc = off + (c - comp['min_c'])
                out[r][nc] = v
                placed.add((r,nc))
    return out