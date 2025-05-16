from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != bg and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                mi = ma = i
                mj = mk = j
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    mi = min(mi, r); ma = max(ma, r)
                    mj = min(mj, c); mk = max(mk, c)
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == col:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append((col, cells, mi, ma, mj, mk))
    ring_segs = []
    for col, cells, mi, ma, mj, mk in comps:
        H = ma - mi + 1; W = mk - mj + 1
        peri = 2*H + 2*W - 4
        onborder = all(r==mi or r==ma or c==mj or c==mk for r,c in cells)
        if onborder and len(cells) < peri and H>1 and W>1:
            ring_segs.append((col, cells, mi, ma, mj, mk))
    ring_by_col = {}
    for col, cells, mi, ma, mj, mk in ring_segs:
        ring_by_col.setdefault(col, []).extend(cells)
    ring_comps = []
    for col, cells in ring_by_col.items():
        rs = cells
        mi = min(r for r,c in rs); ma = max(r for r,c in rs)
        mj = min(c for r,c in rs); mk = max(c for r,c in rs)
        ring_comps.append((col, rs, mi, ma, mj, mk))
    ring_comps.sort(key=lambda x: x[2])
    small_comps = []
    ring_cols = {col for col, *_ in ring_comps}
    for col, cells, mi, ma, mj, mk in comps:
        if col in ring_cols: continue
        small_comps.append((col, cells, mi, ma, mj, mk))
    out = []
    for col, cells, mi, ma, mj, mk in ring_comps:
        H = ma - mi + 1; W = mk - mj + 1
        holes = set()
        for di in range(H):
            for dj in range(W):
                if grid[mi+di][mj+dj] != col:
                    holes.add((di, dj))
        sub = [[col]*W for _ in range(H)]
        shapes = []
        for scol, scells, smi, sma, smj, smk in small_comps:
            ph = set((r-smi, c-smj) for r,c in scells)
            h = sma - smi + 1; w = smk - smj + 1
            shapes.append((len(ph), ph, h, w, scol))
        shapes.sort(reverse=True, key=lambda x: x[0])
        for _, pattern, h, w, sc in shapes:
            placed = False
            for i in range(H-h+1):
                for j in range(W-w+1):
                    region = {(r+i, c+j) for r,c in pattern}
                    if region <= holes:
                        holes -= region
                        for r,c in region:
                            sub[r][c] = sc
                        placed = True
                        break
                if placed: break
        for row in sub:
            out.append(row)
    return out