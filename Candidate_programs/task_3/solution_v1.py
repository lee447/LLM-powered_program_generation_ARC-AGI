from collections import deque
def solve(grid):
    R = len(grid)
    if R==0: 
        return grid
    C = len(grid[0])
    out = [row[:] for row in grid]
    comp = [[-1]*C for _ in range(R)]
    comp_id = 0
    comps = {}
    for i in range(R):
        for j in range(C):
            if grid[i][j] and comp[i][j] < 0:
                q = deque()
                q.append((i,j))
                comp[i][j] = comp_id
                comp_cells = [(i,j)]
                minr, maxr = i, i
                minc, maxc = j, j
                while q:
                    r,c = q.popleft()
                    if r < minr: minr = r
                    if r > maxr: maxr = r
                    if c < minc: minc = c
                    if c > maxc: maxc = c
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<R and 0<=nc<C and grid[nr][nc] and comp[nr][nc] < 0:
                            comp[nr][nc] = comp_id
                            q.append((nr,nc))
                            comp_cells.append((nr,nc))
                comps[comp_id] = {"cells":comp_cells, "minr":minr, "maxr":maxr, "minc":minc, "maxc":maxc}
                comp_id += 1
    # Process each component.
    # For each row that is not the topmost or bottommost of the component,
    # break the set of columns (in that row belonging to the comp) into contiguous segments.
    # For each segment of length >=3, change some interior cells.
    for cid,data in comps.items():
        cells = data["cells"]
        minr, maxr = data["minr"], data["maxr"]
        # Group by row
        rows = {}
        for r,c in cells:
            rows.setdefault(r, []).append(c)
        for r, cols in rows.items():
            # Only process interior rows of the component.
            if r==minr or r==maxr:
                continue
            cols = sorted(cols)
            segs = []
            seg = [cols[0]]
            for idx in range(1, len(cols)):
                if cols[idx] == cols[idx-1] + 1:
                    seg.append(cols[idx])
                else:
                    segs.append(seg)
                    seg = [cols[idx]]
            segs.append(seg)
            for seg in segs:
                if len(seg) < 3:
                    continue
                # Determine accent color for this contiguous horizontal segment.
                accent = None
                for c in seg:
                    if grid[r][c] != 1:
                        accent = grid[r][c]
                        break
                if accent is None:
                    # fallback: if the overall component is tall then use 2,
                    # otherwise use 2 as well.
                    accent = 2
                # Determine how many interior cells there are.
                interior = seg[1:-1]
                L = len(interior)
                # If few interior cells, recolor all; if many, recolor only the boundary of the interior.
                if L < 4:
                    for c in interior:
                        out[r][c] = accent
                elif L < 6:
                    out[r][seg[1]] = accent
                    out[r][seg[-2]] = accent
                else:
                    out[r][seg[1]] = accent
                    out[r][seg[2]] = accent
                    out[r][seg[-2]] = accent
                    out[r][seg[-3]] = accent
    return out