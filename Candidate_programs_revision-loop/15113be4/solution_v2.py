def solve(grid):
    # identify border rows and cols (all 4s)
    n = len(grid)
    m = len(grid[0])
    brow = [i for i in range(n) if all(grid[i][j]==4 for j in range(m))]
    bcol = [j for j in range(m) if all(grid[i][j]==4 for i in range(n))]
    # find content row intervals
    rows = [i for i in range(n) if i not in brow]
    cols = [j for j in range(m) if j not in bcol]
    def intervals(a):
        iv=[];i=0
        while i<len(a):
            j=i
            while j+1<len(a) and a[j+1]==a[j]+1: j+=1
            iv.append(a[i:j+1]); i=j+1
        return iv
    rints = intervals(rows)
    cints = intervals(cols)
    # block size
    br = len(rints[0]); bc = len(cints[0])
    # find template color
    cs = set(v for row in grid for v in row if v not in (0,1,4))
    if not cs:
        return grid
    tc = cs.pop()
    # gather masks from blocks containing tc
    from collections import Counter
    cnt = Counter()
    masks = {}
    for bi,ri in enumerate(rints):
        for bj,ci in enumerate(cints):
            mask = []
            got = False
            for di in range(br):
                row = []
                for dj in range(bc):
                    if grid[ri[di]][ci[dj]]==tc:
                        row.append(1); got=True
                    else:
                        row.append(0)
                mask.append(tuple(row))
            if got:
                t = tuple(mask)
                cnt[t]+=1
                masks[t] = mask
    if not cnt:
        return grid
    # choose most common mask
    msk = max(cnt, key=lambda x: cnt[x])
    mask = masks[msk]
    # apply mask to blocks without tc
    ans = [row[:] for row in grid]
    for ri in rints:
        for ci in cints:
            # skip template blocks
            has_tc = any(grid[ri[di]][ci[dj]]==tc for di in range(br) for dj in range(bc))
            if has_tc:
                continue
            # apply if any 1
            if any(grid[ri[di]][ci[dj]]==1 for di in range(br) for dj in range(bc)):
                for di in range(br):
                    for dj in range(bc):
                        if mask[di][dj] and grid[ri[di]][ci[dj]]==1:
                            ans[ri[di]][ci[dj]] = tc
    return ans