def solve(grid):
    H = len(grid)
    W = len(grid[0])
    run_threshold = 3
    row_flag = [False]*H
    for r in range(H):
        cnt = 0
        for c in range(W):
            if grid[r][c]!=0:
                cnt+=1
                if cnt>=run_threshold:
                    row_flag[r] = True
                    break
            else:
                cnt = 0
    blocks = []
    r = 0
    while r < H:
        if row_flag[r]:
            start = r
            while r+1<H and row_flag[r+1]:
                r+=1
            blocks.append((start, r))
        r+=1
    new = [[0]*W for _ in range(H)]
    def mode(lst):
        d={}
        for x in lst:
            d[x]=d.get(x,0)+1
        m=None;mv=-1
        for x,v in d.items():
            if v>mv:
                mv=v; m=x
        return m
    for (r0,r1) in blocks:
        bh = r1-r0+1
        thresh = (bh+1)//2
        col_ok = [0]*W
        for c in range(W):
            cnt = 0
            for r in range(r0,r1+1):
                if grid[r][c]!=0:
                    cnt+=1
            col_ok[c] = cnt>=thresh
        intervals = []
        c=0
        while c<W:
            if col_ok[c]:
                s=c
                while c+1<W and col_ok[c+1]:
                    c+=1
                intervals.append((s,c))
            c+=1
        for (c1,c2) in intervals:
            width = c2-c1+1
            mixed_rows = []
            uniform_rows = []
            for r in range(r0,r1+1):
                vals = set()
                for c in range(c1,c2+1):
                    v=grid[r][c]
                    if v!=0:
                        vals.add(v)
                if len(vals)<=1:
                    uniform_rows.append(r)
                else:
                    mixed_rows.append(r)
            pattern = [0]*width
            if mixed_rows:
                for k in range(width):
                    vals=[]
                    for r in mixed_rows:
                        v=grid[r][c1+k]
                        if v!=0:
                            vals.append(v)
                    if vals:
                        pattern[k]=mode(vals)
            for r in uniform_rows:
                vals=[]
                for c in range(c1,c2+1):
                    v=grid[r][c]
                    if v!=0:
                        vals.append(v)
                if vals:
                    mc = mode(vals)
                    for c in range(c1,c2+1):
                        new[r][c] = mc
            for r in mixed_rows:
                for k in range(width):
                    new[r][c1+k] = pattern[k]
    return new