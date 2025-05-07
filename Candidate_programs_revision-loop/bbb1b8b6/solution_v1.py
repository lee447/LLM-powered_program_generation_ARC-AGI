from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    sep = next(j for j,v in enumerate(grid[0]) if v==5)
    left = [row[:sep] for row in grid]
    right = [row[sep+1:] for row in grid]
    def extract(half: List[List[int]]) -> Tuple[set, int]:
        pts = set()
        col = None
        for i,row in enumerate(half):
            for j,v in enumerate(row):
                if v!=0:
                    pts.add((i,j))
                    col = v
        return pts, col
    L, cL = extract(left)
    R, cR = extract(right)
    def components(pts: set) -> int:
        vis = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        comps = 0
        for p in pts:
            if p not in vis:
                comps += 1
                stack = [p]
                vis.add(p)
                while stack:
                    x,y = stack.pop()
                    for dx,dy in dirs:
                        q = (x+dx, y+dy)
                        if q in pts and q not in vis:
                            vis.add(q)
                            stack.append(q)
        return comps
    if L.isdisjoint(R):
        w = len(left[0])
        out = [[0]*w for _ in range(h)]
        for i,j in L:
            out[i][j] = cL
        for i,j in R:
            out[i][j] = cR
        return out
    cLnum = components(L)
    cRnum = components(R)
    if cLnum < cRnum:
        return left
    if cRnum < cLnum:
        return right
    if len(L) >= len(R):
        return left
    return right