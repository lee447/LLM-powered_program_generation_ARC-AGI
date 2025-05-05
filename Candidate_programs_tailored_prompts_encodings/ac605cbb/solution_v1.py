from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]!=0]
    taken = set((r,c) for r,c,v in orig)
    out = [[0]*w for _ in range(h)]
    for r,c,v in orig:
        out[r][c] = v
    segments = []
    for r,c,v in orig:
        best = None
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            steps = 0
            rr,cc = r,c
            while True:
                rr+=dr; cc+=dc
                if not (0<=rr<h and 0<=cc<w): break
                if (rr,cc) in taken: break
                steps+=1
                cand = (rr,cc)
                seg = []
                rr2,cc2 = r,c
                for _ in range(steps):
                    rr2+=dr; cc2+=dc
                    seg.append((rr2,cc2))
                ok = True
                for x,y in seg:
                    if out[x][y]!=0: ok=False
                if ok:
                    length = steps
                    if best is None or length<best[0] or (length==best[0] and (dr,dc)<best[1]):
                        best = (length,(dr,dc),cand,seg)
            # end while
        # end for dirs
        if best:
            length,(dr,dc),(rr,cc),seg = best
            taken.add((rr,cc))
            out[rr][cc] = v
            for x,y in seg:
                out[x][y] = 5
            if len(seg)>2:
                mid = seg[len(seg)//2]
                out[mid[0]][mid[1]] = 4
    return out