from collections import deque
def solve(grid):
    R, C = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def neighbors(r,c):
        for dr,dc in dirs:
            rr,cc = r+dr, c+dc
            if 0 <= rr < R and 0 <= cc < C:
                yield rr,cc
    bi = bj = None
    block_vals = {}
    for i in range(R-1):
        for j in range(C-1):
            s = {grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]}
            if 0 in s: continue
            if len(s)==4:
                bi,bj = i,j
                block_vals = {(0,0):grid[i][j], (0,1):grid[i][j+1], (1,0):grid[i+1][j], (1,1):grid[i+1][j+1]}
                break
        if bi is not None: break
    block_colors = set(block_vals.values())
    border_color = None
    for dr,dc in block_vals:
        r,c = bi+dr, bj+dc
        for rr,cc in neighbors(r,c):
            v = grid[rr][cc]
            if v!=0 and v not in block_colors:
                border_color = v
                start = (rr,cc)
                break
        if border_color is not None: break
    dq = deque([start])
    seen = {start}
    border = []
    while dq:
        r,c = dq.popleft()
        border.append((r,c))
        for rr,cc in neighbors(r,c):
            if (rr,cc) not in seen and grid[rr][cc]==border_color:
                seen.add((rr,cc))
                dq.append((rr,cc))
    outmap = {}
    for r,c in border:
        for (dr,dc),v in block_vals.items():
            nr,nc = r+dr, c+dc
            outmap[(nr,nc)] = v
    rows = [r for r,_ in outmap]
    cols = [c for _,c in outmap]
    minr,maxr = min(rows), max(rows)
    minc,maxc = min(cols), max(cols)
    H,W = maxr-minr+1, maxc-minc+1
    out = [[0]*W for _ in range(H)]
    for (r,c),v in outmap.items():
        out[r-minr][c-minc] = v
    return out