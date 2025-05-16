from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    bg = grid[0][0]
    vis = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if not vis[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                mi, ma, mj, mk = i, i, j, j
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    if r<mi: mi=r
                    if r>ma: ma=r
                    if c<mj: mj=c
                    if c>mk: mk=c
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<R and 0<=nc<C and not vis[nr][nc] and grid[nr][nc]==col:
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                comps.append((col, cells, mi, ma, mj, mk))
    ring = []
    small = []
    for col, cells, mi, ma, mj, mk in comps:
        H = ma-mi+1
        W = mk-mj+1
        peri = 2*H+2*W-4
        onborder = all(r==mi or r==ma or c==mj or c==mk for r,c in cells)
        if onborder and len(cells) < peri:
            ring.append((col, cells, mi, ma, mj, mk))
        else:
            small.append((col, cells, mi, ma, mj, mk))
    small_map = {}
    for col, cells, mi, ma, mj, mk in small:
        pattern = frozenset(((r-mi, c-mj) for r,c in cells))
        small_map[(pattern, ma-mi+1, mk-mj+1)] = col
    ring.sort(key=lambda x: x[2])
    out = []
    for col, cells, mi, ma, mj, mk in ring:
        H = ma-mi+1
        W = mk-mj+1
        sub = [[col]*W for _ in range(H)]
        holes = set()
        for i in range(H):
            for j in range(W):
                if grid[mi+i][mj+j] != col:
                    holes.add((i,j))
        while holes:
            stack = [holes.pop()]
            comp = [stack[0]]
            for r,c in stack:
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if (nr,nc) in holes:
                        holes.remove((nr,nc))
                        stack.append((nr,nc))
                        comp.append((nr,nc))
            mis = min(r for r,c in comp)
            mjs = min(c for r,c in comp)
            pattern = frozenset(((r-mis, c-mjs) for r,c in comp))
            key = (pattern, max(r for r,c in comp)-mis+1, max(c for r,c in comp)-mjs+1)
            color = small_map[key]
            for r,c in comp:
                sub[r][c] = color
        for row in sub:
            out.append(row)
    return out