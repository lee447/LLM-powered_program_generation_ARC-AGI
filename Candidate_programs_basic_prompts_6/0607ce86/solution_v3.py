def solve(grid):
    R=len(grid); C=len(grid[0])
    row_segs=[]; in_seg=False
    for y in range(R):
        if any(grid[y][x]!=0 for x in range(C)):
            if not in_seg:
                rs=y; in_seg=True
        else:
            if in_seg:
                row_segs.append((rs,y-1)); in_seg=False
    if in_seg:
        row_segs.append((rs,R-1))
    col_segs=[]; in_seg=False
    for x in range(C):
        if any(grid[y][x]!=0 for y in range(R)):
            if not in_seg:
                cs=x; in_seg=True
        else:
            if in_seg:
                col_segs.append((cs,x-1)); in_seg=False
    if in_seg:
        col_segs.append((cs,C-1))
    blocks=[]
    for r1,r2 in row_segs:
        for c1,c2 in col_segs:
            anynz=False
            for y in range(r1,r2+1):
                for x in range(c1,c2+1):
                    if grid[y][x]!=0:
                        anynz=True; break
                if anynz: break
            if anynz:
                blocks.append((r1,c1))
    if not blocks:
        return [[0]*C for _ in range(R)]
    H=row_segs[0][1]-row_segs[0][0]+1
    W=col_segs[0][1]-col_segs[0][0]+1
    template=[[0]*W for _ in range(H)]
    for dy in range(H):
        for dx in range(W):
            cnt={}
            for r1,c1 in blocks:
                v=grid[r1+dy][c1+dx]
                if v!=0:
                    cnt[v]=cnt.get(v,0)+1
            if cnt:
                mv=max(cnt.values())
                for k,v0 in cnt.items():
                    if v0==mv:
                        template[dy][dx]=k
                        break
    out=[[0]*C for _ in range(R)]
    for r1,c1 in blocks:
        for dy in range(H):
            for dx in range(W):
                out[r1+dy][c1+dx]=template[dy][dx]
    return out