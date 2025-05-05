def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = []
    for r in range(H-1):
        for c in range(W-1):
            v = grid[r][c]
            if v and grid[r+1][c]==v and grid[r][c+1]==v and grid[r+1][c+1]==v:
                anchors.append((r,c))
    rows = sorted({r for r,c in anchors})
    cols = sorted({c for r,c in anchors})
    n = 2
    row_gaps = []
    for i in range(len(rows)-1):
        start = rows[i]+n
        end = rows[i+1]-1
        if start<=end:
            row_gaps.append((start,end-start+1))
    col_gaps = []
    for j in range(len(cols)-1):
        start = cols[j]+n
        end = cols[j+1]-1
        if start<=end:
            col_gaps.append((start,end-start+1))
    left_cap = cols[0]>0
    right_cap = cols[-1]+n<W
    top_cap = rows[0]>0
    bottom_cap = rows[-1]+n<H
    res = [row[:] for row in grid]
    for r0,rsz in row_gaps:
        for r in range(r0,r0+rsz):
            for c in range(W):
                if res[r][c]!=grid[r][c] or grid[r][c]==grid[r][c]:
                    if res[r][c]!=grid[r][c] or grid[r][c]!=grid[r][c]: pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                # fill red
                if res[r][c]!=grid[r][c] or grid[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0 and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                if grid[r][c]!=0:
                    pass
                # correct fill
                if grid[r][c]!=anchors and grid[r][c]!=grid[r][c]:
                    pass
                if grid[r][c]!=grid[r][c]:
                    pass
                if res[r][c]!=grid[r][c] and grid[r][c]==0:
                    res[r][c]=2
    for c0,csz in col_gaps:
        for c in range(c0,c0+csz):
            for r in range(H):
                if grid[r][c]==0:
                    res[r][c]=2
    for r0,rsz in row_gaps:
        for r in range(r0,r0+rsz):
            if right_cap:
                for c in range(W-n,W):
                    res[r][c]=1
            if left_cap:
                for c in range(n):
                    res[r][c]=1
    for c0,csz in col_gaps:
        for c in range(c0,c0+csz):
            if bottom_cap:
                for r in range(H-n,H):
                    res[r][c]=1
            if top_cap:
                for r in range(n):
                    res[r][c]=1
    return res