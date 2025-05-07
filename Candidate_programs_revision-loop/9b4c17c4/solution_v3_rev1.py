from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    cells = [(i, j, grid[i][j]) for i in range(H) for j in range(W)]
    vals = set(c for _, _, c in cells if c != 0)
    fg = next(c for c in vals if sum(1 for _, _, v in cells if v == c) < H * W)
    bgs = [c for c in vals if c != fg]
    def bbox(color: int) -> Tuple[int,int,int,int]:
        xs = [i for i,j,c in cells if c == color]
        ys = [j for i,j,c in cells if c == color]
        return min(xs), max(xs), min(ys), max(ys)
    b0 = bbox(bgs[0]); b1 = bbox(bgs[1])
    hpart = (b0[2] == 0 and b0[3] == W-1 and b1[2] == 0 and b1[3] == W-1)
    vpart = (b0[0] == 0 and b0[1] == H-1 and b1[0] == 0 and b1[1] == H-1)
    out = [row[:] for row in grid]
    # gather components of fg
    seen = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i,j,c in cells:
        if c==fg and not seen[i][j]:
            q=[(i,j)]; seen[i][j]=True; comp=[]
            while q:
                x,y=q.pop(); comp.append((x,y))
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==fg:
                        seen[nx][ny]=True; q.append((nx,ny))
            comps.append(comp)
    for comp in comps:
        rs=[x for x,_ in comp]; cs=[y for _,y in comp]
        r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
        # determine region
        bg = grid[r0][minc-1] if minc>0 and grid[r0][minc-1]!=fg else grid[r0][maxc+1] if maxc<W-1 else None
        if bg is None:
            bg = bgs[0]
        br0,br1,bc0,bc1 = bbox(bg)
        for x,y in comp:
            out[x][y]=bg
        if vpart:
            if bg==bgs[0]:
                newc0 = bc1 - (maxc-minc)
            else:
                newc0 = bc0
        else:
            if bg==bgs[0]:
                newc0 = bc0
            else:
                newc0 = bc1 - (maxc-minc)
        for x,y in comp:
            out[x][newc0 + (y-minc)] = fg
    return out