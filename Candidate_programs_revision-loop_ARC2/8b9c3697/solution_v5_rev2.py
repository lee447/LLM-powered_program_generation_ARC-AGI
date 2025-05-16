from collections import deque, Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = Counter(grid[r][c] for r in range(h) for c in range(w))
    bg = cnt.most_common(1)[0][0]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def comps(color):
        seen = [[False]*w for _ in range(h)]
        out = []
        for i in range(h):
            for j in range(w):
                if not seen[i][j] and grid[i][j]==color:
                    q=deque([(i,j)]); seen[i][j]=True; comp=[]
                    while q:
                        x,y=q.popleft(); comp.append((x,y))
                        for dx,dy in dirs:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==color:
                                seen[nx][ny]=True; q.append((nx,ny))
                    out.append(comp)
        return out
    colors=[c for c in cnt if c!=bg]
    cA = next(c for c in colors if len(comps(c))==2 and len(comps(c)[0])==len(comps(c)[1]))
    cB = next(c for c in colors if c!=cA)
    compA_list = comps(cA)
    compB = comps(cB)[0]
    setB = set(compB)
    for compA in compA_list:
        pA_out = pb = None
        for (r,c) in compA:
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if (nr,nc) in setB:
                    pA_out=(r,c); pb=(nr,nc)
                    break
            if pA_out: break
        if not pA_out: continue
        dr,dc = pb[0]-pA_out[0], pb[1]-pA_out[1]
        pin = (pb[0]+dr, pb[1]+dc)
        pts = [(r-pA_out[0]+pin[0], c-pA_out[1]+pin[1]) for (r,c) in compA]
        ok=True
        for rr,cc in pts:
            if not (0<=rr<h and 0<=cc<w and grid[rr][cc]==bg): ok=False; break
        if not ok: continue
        for rr,cc in pts:
            grid[rr][cc]=cA
    return grid