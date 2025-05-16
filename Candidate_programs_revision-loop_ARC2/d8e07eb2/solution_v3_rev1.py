import copy
def solve(grid):
    h,w=len(grid),len(grid[0])
    bg,sep,fill=8,6,3
    out=[row[:] for row in grid]
    rows=[]
    for i in range(1,h-2):
        block=True
        for di in range(3):
            for j in range(w):
                if grid[i+di][j] in (bg,sep):
                    block=False
                    break
            if not block: break
        if block: rows.append(i)
    cols=[]
    if rows:
        r0=rows[0]
        for j in range(1,w-2):
            block=True
            for di in range(3):
                for dj in range(3):
                    if grid[r0+di][j+dj] in (bg,sep):
                        block=False
                        break
                if not block: break
            if block: cols.append(j)
    for r0 in rows:
        for c0 in cols:
            v=grid[r0][c0]
            if v in (bg,sep): continue
            same=True
            for di in range(3):
                for dj in range(3):
                    if grid[r0+di][c0+dj]!=v:
                        same=False
                        break
                if not same: break
            if not same: continue
            for di in range(3):
                for dc in (-1,3):
                    rr,cc=r0+di,c0+dc
                    if 0<=rr<h and 0<=cc<w and out[rr][cc]==bg: out[rr][cc]=fill
            for dj in range(3):
                for dr in (-1,3):
                    rr,cc=r0+dr,c0+dj
                    if 0<=rr<h and 0<=cc<w and out[rr][cc]==bg: out[rr][cc]=fill
    return out