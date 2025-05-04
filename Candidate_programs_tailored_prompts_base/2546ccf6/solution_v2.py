def solve(grid):
    H=len(grid);W=len(grid[0])
    orig=grid
    res=[row[:] for row in grid]
    row_stripes=[r for r in range(H) if grid[r][0]!=0 and all(grid[r][c]==grid[r][0] for c in range(W))]
    col_stripes=[c for c in range(W) if grid[0][c]!=0 and all(grid[r][c]==grid[0][c] for r in range(H))]
    row_stripes.sort();col_stripes.sort()
    rsegs=[]
    prev=0
    for r in row_stripes:
        if prev<r: rsegs.append((prev,r))
        prev=r+1
    if prev<H: rsegs.append((prev,H))
    csegs=[]
    prev=0
    for c in col_stripes:
        if prev<c: csegs.append((prev,c))
        prev=c+1
    if prev<W: csegs.append((prev,W))
    for ri in range(1,len(rsegs)-1):
        r0,r1=rsegs[ri]
        for ci in range(len(csegs)-1):
            c0,c1=csegs[ci]
            cells=[(r,c) for r in range(r0,r1) for c in range(c0,c1) if orig[r][c]!=0]
            if not cells: continue
            color=orig[cells[0][0]][cells[0][1]]
            rel=[(r-r0,c-c0) for r,c in cells]
            dc_index=ci+1
            c2_0,c2_1=csegs[dc_index]
            ok=True
            for dr,dc in rel:
                if res[r0+dr][c2_0+dc]!=0: ok=False; break
            if not ok: continue
            for dr,dc in rel:
                res[r0+dr][c2_0+dc]=color
    return res
def solve(grid):
    H=len(grid);W=len(grid[0])
    orig=grid
    res=[row[:] for row in grid]
    row_stripes=[r for r in range(H) if grid[r][0]!=0 and all(grid[r][c]==grid[r][0] for c in range(W))]
    col_stripes=[c for c in range(W) if grid[0][c]!=0 and all(grid[r][c]==grid[0][c] for r in range(H))]
    row_stripes.sort();col_stripes.sort()
    rsegs=[]
    prev=0
    for r in row_stripes:
        if prev<r: rsegs.append((prev,r))
        prev=r+1
    if prev<H: rsegs.append((prev,H))
    csegs=[]
    prev=0
    for c in col_stripes:
        if prev<c: csegs.append((prev,c))
        prev=c+1
    if prev<W: csegs.append((prev,W))
    for ri in range(1,len(rsegs)-1):
        r0,r1=rsegs[ri]
        for ci in range(len(csegs)-1):
            c0,c1=csegs[ci]
            cells=[(r,c) for r in range(r0,r1) for c in range(c0,c1) if orig[r][c]!=0]
            if not cells: continue
            color=orig[cells[0][0]][cells[0][1]]
            rel=[(r-r0,c-c0) for r,c in cells]
            dc_index=ci+1
            if dc_index>=len(csegs): continue
            c2_0,c2_1=csegs[dc_index]
            ok=True
            for dr,dc in rel:
                if res[r0+dr][c2_0+dc]!=0: ok=False; break
            if not ok: continue
            for dr,dc in rel:
                res[r0+dr][c2_0+dc]=color
    return res
def solve(grid):
    H=len(grid)
    W=len(grid[0])
    orig=grid
    res=[row[:] for row in grid]
    row_stripes=[r for r in range(H) if grid[r][0]!=0 and all(grid[r][c]==grid[r][0] for c in range(W))]
    col_stripes=[c for c in range(W) if grid[0][c]!=0 and all(grid[r][c]==grid[0][c] for r in range(H))]
    row_stripes.sort()
    col_stripes.sort()
    rsegs=[]
    prev=0
    for r in row_stripes:
        if prev<r:
            rsegs.append((prev,r))
        prev=r+1
    if prev<H:
        rsegs.append((prev,H))
    csegs=[]
    prev=0
    for c in col_stripes:
        if prev<c:
            csegs.append((prev,c))
        prev=c+1
    if prev<W:
        csegs.append((prev,W))
    for ri in range(1,len(rsegs)-1):
        r0,r1=rsegs[ri]
        for ci in range(len(csegs)-1):
            c0,c1=csegs[ci]
            cells=[(r,c) for r in range(r0,r1) for c in range(c0,c1) if orig[r][c]!=0]
            if not cells:
                continue
            color=orig[cells[0][0]][cells[0][1]]
            rel=[(r-r0,c-c0) for r,c in cells]
            dc_index=ci+1
            if dc_index>=len(csegs):
                continue
            c2_0,c2_1=csegs[dc_index]
            can_copy=True
            for dr,dc in rel:
                if res[r0+dr][c2_0+dc]!=0:
                    can_copy=False
                    break
            if not can_copy:
                continue
            for dr,dc in rel:
                res[r0+dr][c2_0+dc]=color
    return res
def solve(grid):
    H=len(grid)
    W=len(grid[0])
    orig=grid
    res=[row[:] for row in grid]
    row_stripes=[r for r in range(H) if grid[r][0]!=0 and all(grid[r][c]==grid[r][0] for c in range(W))]
    col_stripes=[c for c in range(W) if grid[0][c]!=0 and all(grid[r][c]==grid[0][c] for r in range(H))]
    row_stripes.sort()
    col_stripes.sort()
    rsegs=[]
    prev=0
    for r in row_stripes:
        if prev<r:
            rsegs.append((prev,r))
        prev=r+1
    if prev<H:
        rsegs.append((prev,H))
    csegs=[]
    prev=0
    for c in col_stripes:
        if prev<c:
            csegs.append((prev,c))
        prev=c+1
    if prev<W:
        csegs.append((prev,W))
    for ri in range(1,len(rsegs)-1):
        r0,r1=rsegs[ri]
        for ci in range(len(csegs)-1):
            c0,c1=csegs[ci]
            cells=[(r,c) for r in range(r0,r1) for c in range(c0,c1) if orig[r][c]!=0]
            if not cells: continue
            color=orig[cells[0][0]][cells[0][1]]
            rel=[(r-r0,c-c0) for r,c in cells]
            dc_index=ci+1
            if dc_index>=len(csegs): continue
            c2_0,c2_1=csegs[dc_index]
            ok=True
            for dr,dc in rel:
                if res[r0+dr][c2_0+dc]!=0:
                    ok=False
                    break
            if not ok: continue
            for dr,dc in rel:
                res[r0+dr][c2_0+dc]=color
    return res
def solve(grid):
    H=len(grid)
    W=len(grid[0])
    orig=grid
    res=[row[:] for row in grid]
    row_stripes=[r for r in range(H) if grid[r][0]!=0 and all(grid[r][c]==grid[r][0] for c in range(W))]
    col_stripes=[c for c in range(W) if grid[0][c]!=0 and all(grid[r][c]==grid[0][c] for r in range(H))]
    row_stripes.sort()
    col_stripes.sort()
    rsegs=[]
    prev=0
    for r in row_stripes:
        if prev<r:
            rsegs.append((prev,r))
        prev=r+1
    if prev<H:
        rsegs.append((prev,H))
    csegs=[]
    prev=0
    for c in col_stripes:
        if prev<c:
            csegs.append((prev,c))
        prev=c+1
    if prev<W:
        csegs.append((prev,W))
    for ri in range(1,len(rsegs)-1):
        r0,r1=rsegs[ri]
        for ci in range(len(csegs)-1):
            c0,c1=csegs[ci]
            cells=[(r,c) for r in range(r0,r1) for c in range(c0,c1) if orig[r][c]!=0]
            if not cells: continue
            color=orig[cells[0][0]][cells[0][1]]
            rel=[(r-r0,c-c0) for r,c in cells]
            dc_index=ci+1
            if dc_index>=len(csegs): continue
            c2_0,c2_1=csegs[dc_index]
            ok=True
            for dr,dc in rel:
                if res[r0+dr][c2_0+dc]!=0:
                    ok=False; break
            if not ok: continue
            for dr,dc in rel:
                res[r0+dr][c2_0+dc]=color
    return res
def solve(grid):
    H=len(grid)
    W=len(grid[0])
    orig=grid
    res=[row[:] for row in grid]
    row_stripes=[r for r in range(H) if grid[r][0]!=0 and all(grid[r][c]==grid[r][0] for c in range(W))]
    col_stripes=[c for c in range(W) if grid[0][c]!=0 and all(grid[r][c]==grid[0][c] for r in range(H))]
    row_stripes.sort()
    col_stripes.sort()
    rsegs=[]
    prev=0
    for r in row_stripes:
        if prev<r: rsegs.append((prev,r))
        prev=r+1
    if prev<H: rsegs.append((prev,H))
    csegs=[]
    prev=0
    for c in col_stripes:
        if prev<c: csegs.append((prev,c))
        prev=c+1
    if prev<W: csegs.append((prev,W))
    for ri in range(1,len(rsegs)-1):
        r0,r1=rsegs[ri]
        for ci in range(len(csegs)-1):
            c0,c1=csegs[ci]
            cells=[(r,c) for r in range(r0,r1) for c in range(c0,c1) if orig[r][c]!=0]
            if not cells: continue
            color=orig[cells[0][0]][cells[0][1]]
            rel=[(r-r0,c-c0) for r,c in cells]
            dc_index=ci+1
            if dc_index>=len(csegs): continue
            c2_0,c2_1=csegs[dc_index]
            ok=True
            for dr,dc in rel:
                if res[r0+dr][c2_0+dc]!=0:
                    ok=False
                    break
            if not ok: continue
            for dr,dc in rel:
                res[r0+dr][c2_0+dc]=color
    return res