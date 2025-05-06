def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    cells = {(r,c) for r in range(h) for c in range(w) if grid[r][c]==5}
    if not cells:
        return []
    # find largest component by 4-adjacency
    seen = set()
    best = set()
    for cell in cells:
        if cell in seen: continue
        stack = [cell]
        comp = {cell}
        seen.add(cell)
        while stack:
            r,c = stack.pop()
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr,nc) in cells and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    comp.add((nr,nc))
                    stack.append((nr,nc))
        if len(comp)>len(best):
            best = comp
    comp = best
    # build neighbor map
    neigh = {cell:[] for cell in comp}
    for r,c in comp:
        for dr,dc in dirs:
            if (r+dr,c+dc) in comp:
                neigh[(r,c)].append((r+dr,c+dc))
    # find start
    ends = [p for p,v in neigh.items() if len(v)==1]
    start = ends[0] if ends else next(iter(comp))
    path = [start]
    prev = None
    cur = start
    visited = {start}
    dirs_map = {(-1,0):0,(0,1):1,(1,0):2,(0,-1):3}
    changes = 0
    prev_d = None
    while True:
        cand = [n for n in neigh[cur] if n!=prev and n not in visited]
        if not cand:
            break
        nxt = cand[0]
        dr = nxt[0]-cur[0], nxt[1]-cur[1]
        d = dirs_map.get(dr)
        if prev_d is not None and d!=prev_d:
            changes += 1
        prev_d = d
        prev, cur = cur, nxt
        visited.add(nxt)
        path.append(nxt)
    return [[0] for _ in range(changes)]