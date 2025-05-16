from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    reps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                c = grid[i][j]
                stack = [(i,j)]
                vis[i][j] = True
                minr, minc = i, j
                while stack:
                    r, cc = stack.pop()
                    if r < minr or (r == minr and cc < minc):
                        minr, minc = r, cc
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == c:
                            vis[nr][nc] = True
                            stack.append((nr, nc))
                reps.append((minr, minc, grid[minr][minc]))
    rs = sorted({r for r,_,_ in reps})
    cs = sorted({c for _,c,_ in reps})
    drs = [rs[i+1]-rs[i] for i in range(len(rs)-1) if rs[i+1]-rs[i] > 1]
    dcs = [cs[i+1]-cs[i] for i in range(len(cs)-1) if cs[i+1]-cs[i] > 1]
    from collections import Counter
    d = drs + dcs
    if d:
        step = Counter(d).most_common(1)[0][0]
    else:
        step = max(h, w)
    H = step-1 if step > 4 else step
    rmod = [r % step for r,_,_ in reps]
    cmod = [c % step for _,c,_ in reps]
    shiftR = Counter(rmod).most_common(1)[0][0]
    shiftC = Counter(cmod).most_common(1)[0][0]
    out = [[0]*w for _ in range(h)]
    for r, c, col in reps:
        if col == 6: continue
        if (r - shiftR) % step or (c - shiftC) % step: continue
        if col in (2,4):
            p_type = 'solid'
            out_col = 4
        elif col in (1,3):
            p_type = 'ring'
            out_col = 1
        elif col == 5:
            p_type = 'quarter'
            out_col = 6
        elif col == 8:
            p_type = 'x'
            out_col = 7
        else:
            continue
        for i in range(H):
            for j in range(H):
                if p_type == 'solid':
                    val = True
                elif p_type == 'ring':
                    val = (i == 0 or i == H-1 or j == 0 or j == H-1)
                elif p_type == 'quarter':
                    val = (i < H//2 and j < H//2) or (i >= H//2 and j >= H//2)
                else:
                    val = (i == j or i + j == H-1)
                if val:
                    out[r+i][c+j] = out_col
    return out