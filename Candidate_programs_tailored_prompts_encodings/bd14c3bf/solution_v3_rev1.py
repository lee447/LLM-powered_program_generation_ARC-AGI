def solve(grid):
    H = len(grid)
    W = len(grid[0])
    comp_id = [[-1]*W for _ in range(H)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    cid = 0
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0 and comp_id[r][c] == -1:
                v = grid[r][c]
                stack = [(r,c)]
                comp_id[r][c] = cid
                cells = []
                while stack:
                    rr,cc = stack.pop()
                    cells.append((rr,cc))
                    for dr,dc in dirs:
                        nr,nc = rr+dr,cc+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == v and comp_id[nr][nc] == -1:
                            comp_id[nr][nc] = cid
                            stack.append((nr,nc))
                comps.append({'coords':cells,'val':v})
                cid += 1
    n = cid
    coords_sets = [set(c['coords']) for c in comps]
    coords_map = {frozenset(s):i for i,s in enumerate(coords_sets)}
    paired = [None]*n
    for i in range(n):
        if paired[i] is None:
            mirrored = {(r, W-1-c) for r,c in comps[i]['coords']}
            j = coords_map.get(frozenset(mirrored))
            if j is not None and j != i and paired[j] is None:
                paired[i] = j
                paired[j] = i
    centroids = [sum(c for r,c in comps[i]['coords'])/len(comps[i]['coords']) for i in range(n)]
    new_color = [comps[i]['val'] for i in range(n)]
    for i in range(n):
        j = paired[i]
        if j is not None and i < j:
            if centroids[i] < centroids[j]:
                left,right = i,j
            else:
                left,right = j,i
            c = comps[left]['val']
            new_color[left] = c
            new_color[right] = c
    out = [[0]*W for _ in range(H)]
    for i in range(n):
        c = new_color[i]
        for r,c2 in comps[i]['coords']:
            out[r][c2] = c
    return out