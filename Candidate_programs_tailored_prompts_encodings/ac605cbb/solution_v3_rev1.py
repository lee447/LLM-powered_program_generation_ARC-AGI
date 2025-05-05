from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]!=0]
    occupied = set((r,c) for r,c,v in pts)
    out = [[0]*w for _ in range(h)]
    for r,c,v in pts:
        out[r][c]=v
    mids = []
    for r,c,v in pts:
        best = None
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            rr,cc,steps = r,c,0
            while True:
                rr+=dr; cc+=dc
                if not (0<=rr<h and 0<=cc<w): break
                if (rr,cc) in occupied: break
                steps+=1
                cand = (rr,cc)
                seg = []
                tr,tc = r,c
                for _ in range(steps):
                    tr+=dr; tc+=dc
                    seg.append((tr,tc))
                ok = all(out[x][y]==0 for x,y in seg)
                if ok:
                    if best is None or steps<best[0] or (steps==best[0] and (dr,dc)<best[1]):
                        best = (steps,(dr,dc),cand,seg)
        if best:
            length,(dr,dc),(er,ec),seg = best
            occupied.add((er,ec))
            out[er][ec]=v
            for x,y in seg: out[x][y]=5
            if len(seg)>2:
                mr,mc = seg[len(seg)//2]
                out[mr][mc]=4
                mids.append((mr,mc))
    for mr,mc in mids:
        best = None
        for ddr,ddc in ((1,1),(1,-1),(-1,1),(-1,-1)):
            steps=0
            rr,cc = mr,mc
            while True:
                rr+=ddr; cc+=ddc
                if not (0<=rr<h and 0<=cc<w): break
                if out[rr][cc]!=0: break
                steps+=1
            if best is None or steps>best[0] or (steps==best[0] and (ddr,ddc)>best[1]):
                best=(steps,(ddr,ddc))
        if best and best[0]>0:
            ddr,ddc = best[1]
            rr,cc = mr,mc
            while True:
                rr+=ddr; cc+=ddc
                if not (0<=rr<h and 0<=cc<w) or out[rr][cc]!=0: break
                out[rr][cc]=4
    return out